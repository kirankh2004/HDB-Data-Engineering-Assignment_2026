"""
profiler.py

Generate a text-based profiling report containing dataset statistics,
schema details, null counts, and distinct value counts.
"""


from pyspark.sql.functions import col

from src.config import REPORTS_PATH


def profile_dataset(df):
    """
    Generate a basic profiling report.
    """

    REPORTS_PATH.mkdir(parents=True, exist_ok=True)

    report_file = REPORTS_PATH / "data_profile.txt"

    with open(report_file, "w") as f:

        f.write("HDB DATA PROFILE REPORT\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"Total Records : {df.count()}\n")
        f.write(f"Total Columns : {len(df.columns)}\n\n")

        f.write("COLUMN DETAILS\n")
        f.write("-" * 60 + "\n")

        for field in df.schema.fields:
            f.write(f"{field.name:<25} {field.dataType}\n")

        f.write("\nNULL COUNTS\n")
        f.write("-" * 60 + "\n")

        for column in df.columns:
            null_count = df.filter(col(column).isNull()).count()
            f.write(f"{column:<25} {null_count}\n")

        f.write("\nDISTINCT COUNTS\n")
        f.write("-" * 60 + "\n")

        for column in df.columns:
            distinct_count = df.select(column).distinct().count()
            f.write(f"{column:<25} {distinct_count}\n")

    print(f"Profile report saved to {report_file}")