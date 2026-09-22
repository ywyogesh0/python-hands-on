from pyspark.sql import SparkSession
from pyspark.sql.functions import col

payments = [
    ("P1", "C1", 100.0, "2026-09-21", "SUCCESS"),
    ("P1", "C1", 120.0, "2026-09-21", "SUCCESS"),
    ("P2", "C2", 200.0, "2026-09-22", "FAILURE"),
    ("P2", "C2", 250.0, "2026-09-22", "SUCCESS"),
    ("P3", "C3", 500.0, "2026-09-23", "SUCCESS")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_6")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

import tempfile
with tempfile.TemporaryDirectory(prefix="save") as tmpdir:
    df = spark.createDataFrame(
        payments,
        schema = ["payment_id", "customer_id", "amount", "processing_date", "status"]
    )

    df.write.format(
        "parquet"
    ).mode(
        "overwrite"
    ).partitionBy(
        "processing_date"
    ).save(
        tmpdir
    )

    df_2 = spark.read.parquet(tmpdir).filter(
        (col("processing_date") == "2026-09-21") &
        (col("amount") > 100)
    )

    df_2.explain(True)
    df_2.show()

spark.stop()

