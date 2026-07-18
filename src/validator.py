"""
validator.py

Performs data validation and anomaly detection on the HDB resale dataset.
"""

from pyspark.sql.functions import col, lit


def validate_dataset(df):
    """
    Validate the dataset and separate valid and invalid records.

    Returns:
        valid_df: Records that pass all validation checks.
        failed_df: Records that fail one or more validation checks.
    """

    # Valid values derived from the dataset
    valid_towns = [r[0] for r in df.select("town").distinct().collect()]
    valid_flat_types = [r[0] for r in df.select("flat_type").distinct().collect()]
    valid_flat_models = [r[0] for r in df.select("flat_model").distinct().collect()]
    valid_storey_ranges = [r[0] for r in df.select("storey_range").distinct().collect()]

    valid_df = df.filter(
        col("month").isNotNull()
        & col("town").isin(valid_towns)
        & col("flat_type").isin(valid_flat_types)
        & col("flat_model").isin(valid_flat_models)
        & col("storey_range").isin(valid_storey_ranges)
    )

    failed_df = df.subtract(valid_df).withColumn(
        "failure_reason",
        lit("Validation Failed")
    )

    return valid_df, failed_df





def detect_price_anomalies(df):
    """
    Detect resale price anomalies using the Interquartile Range (IQR) method.

    Returns:
        clean_df: Records with resale prices within the acceptable IQR range.
        failed_df: Records identified as anomalous resale price outliers.
    """

    q1, q3 = df.approxQuantile("resale_price", [0.25, 0.75], 0.01)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    clean_df = df.filter(
        (col("resale_price") >= lower) &
        (col("resale_price") <= upper)
    )

    failed_df = (
        df.filter(
            (col("resale_price") < lower) |
            (col("resale_price") > upper)
        )
        .withColumn(
            "failure_reason",
            lit("Anomalous Resale Price")
        )
    )

    return clean_df, failed_df