"""
cleaner.py

Data cleaning functions.
"""

from pyspark.sql.functions import (
    col,
    current_date,
    year,
    month,
    floor,
    concat,
    lit
)


def recompute_remaining_lease(df):
    """
    Recompute remaining lease assuming HDB lease is 99 years.
    """

    current_year = year(current_date())

    lease_end_year = col("lease_commence_date") + 99

    remaining_months = (
        (lease_end_year - current_year) * 12
        - (month(current_date()) - 1)
    )

    remaining_years = floor(remaining_months / 12)

    remaining_months_only = remaining_months % 12

    return (
        df.drop("remaining_lease")
          .withColumn(
              "remaining_lease",
              concat(
                  remaining_years.cast("string"),
                  lit(" Years "),
                  remaining_months_only.cast("string"),
                  lit(" Months")
              )
          )
    )


from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc, lit


def remove_duplicate_records(df):
    """
    Keep the highest resale_price for duplicate records.
    Duplicate key = all columns except resale_price.
    """

    business_key = [
        "month",
        "town",
        "flat_type",
        "block",
        "street_name",
        "storey_range",
        "floor_area_sqm",
        "flat_model",
        "lease_commence_date",
        "remaining_lease"
    ]

    window_spec = (
        Window.partitionBy(*business_key)
        .orderBy(desc("resale_price"))
    )

    ranked_df = df.withColumn(
        "row_num",
        row_number().over(window_spec)
    )

    clean_df = (
        ranked_df
        .filter("row_num = 1")
        .drop("row_num")
    )

    failed_df = (
        ranked_df
        .filter("row_num > 1")
        .drop("row_num")
        .withColumn(
            "failure_reason",
            lit("Duplicate Record - Lower Resale Price")
        )
    )

    return clean_df, failed_df