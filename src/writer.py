"""
writer.py

Writes DataFrames to disk.
"""

from src.config import (
    CLEANED_PATH,
    FAILED_PATH,
    TRANSFORMED_PATH,
    HASHED_PATH
)


def write_cleaned(df):

    (
        df.write
        .mode("overwrite")
        .parquet(str(CLEANED_PATH))
    )

    print(f"✓ Cleaned data written to {CLEANED_PATH}")


def write_failed(df):

    (
        df.write
        .mode("overwrite")
        .parquet(str(FAILED_PATH))
    )

    print(f"✓ Failed data written to {FAILED_PATH}")


def write_transformed(df):

    (
        df.write
        .mode("overwrite")
        .parquet(str(TRANSFORMED_PATH))
    )

    print(f"✓ Transformed data written to {TRANSFORMED_PATH}")


def write_hashed(df):
    """
    Write the hashed dataset to the hashed output directory.
    """

    (
        df.write
        .mode("overwrite")
        .parquet(str(HASHED_PATH))
    )

    print(f"✓ Hashed data written to {HASHED_PATH}")