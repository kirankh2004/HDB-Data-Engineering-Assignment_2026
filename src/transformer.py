"""
transformer.py

Performs business transformations on the HDB resale dataset.
"""

from pyspark.sql import Window
from pyspark.sql.functions import (
    avg,
    col,
    regexp_extract,
    lpad,
    floor,
    substring,
    date_format,
    upper,
    concat,
    lit
)


def generate_resale_identifier(df):
    """
    Generate a unique resale identifier using selected business attributes.
    """

    window_spec = Window.partitionBy(
        "month",
        "town",
        "flat_type"
    )

    df = df.withColumn(
        "avg_price",
        avg("resale_price").over(window_spec)
    )

    df = (
        df.withColumn(
            "block_digits",
            lpad(
                regexp_extract(col("block"), r"(\d+)", 1),
                3,
                "0"
            )
        )
        .withColumn(
            "avg_digits",
            substring(
                floor(col("avg_price")).cast("string"),
                1,
                2
            )
        )
        .withColumn(
            "month_digits",
            date_format(col("month"), "MM")
        )
        .withColumn(
            "town_initial",
            substring(
                upper(col("town")),
                1,
                1
            )
        )
        .withColumn(
            "resale_identifier",
            concat(
                lit("S"),
                col("block_digits"),
                col("avg_digits"),
                col("month_digits"),
                col("town_initial")
            )
        )
        .drop(
            "avg_price",
            "block_digits",
            "avg_digits",
            "month_digits",
            "town_initial"
        )
    )

    return df