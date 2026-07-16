from pyspark.sql import SparkSession


def create_spark():

    spark = (
        SparkSession.builder
        .appName("HDB_DE_Assignment_2026")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark