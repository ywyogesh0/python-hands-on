from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, to_timestamp
from pyspark.sql import Window


payments = [
    ("P1", "C1", 100.0, "2026-09-21 10:00:00"),
    ("P1", "C1", 120.0, "2026-09-21 10:05:00"),
    ("P2", "C2", 200.0, "2026-09-21 09:00:00"),
    ("P2", "C2", 250.0, "2026-09-21 11:00:00"),
    ("P3", "C3", 500.0, "2026-09-21 08:00:00")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_4")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    payments,
    schema = ["payment_id", "customer_id", "amount", "timestamp"]
).withColumn(
    "timestamp",
    to_timestamp(
        "timestamp",
        "yyyy-MM-dd HH:mm:ss"
    )
)

window_spec = Window.partitionBy(
    "payment_id",
).orderBy(
    col("timestamp").desc()
)

df.withColumn(
    "row_number",
    row_number().over(
        window_spec
    )
).filter(
    col("row_number") == 1
).drop(
    "row_number"
).show()

spark.stop()

