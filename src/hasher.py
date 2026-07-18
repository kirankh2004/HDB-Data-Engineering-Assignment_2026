"""
hasher.py

Applies SHA-256 hashing to the generated resale identifier.
"""

from pyspark.sql.functions import sha2, col


def hash_resale_identifier(df):
    """
    Hash resale_identifier using SHA-256.
    """

    return df.withColumn(
        "hashed_resale_identifier",
        sha2(col("resale_identifier"), 256)
    )