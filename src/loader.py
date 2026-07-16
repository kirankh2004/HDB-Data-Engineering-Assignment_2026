"""
loader.py

Loads all raw HDB resale datasets into a single master DataFrame.
"""

from pathlib import Path

from pyspark.sql import DataFrame

from src.config import RAW_PATH


def load_master_dataset(spark) -> DataFrame:
    """
    Read all CSV files from data/raw and combine them into one master DataFrame.
    """

    csv_files = sorted(RAW_PATH.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data/raw")

    dataframes = []

    for file in csv_files:

        print(f"Reading {file.name}")

        df = (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(str(file))
        )

        dataframes.append(df)

    master_df = dataframes[0]

    for df in dataframes[1:]:
        master_df = master_df.unionByName(
            df,
            allowMissingColumns=True
        )

    return master_df