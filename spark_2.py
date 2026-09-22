from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col

payments = [
    ("P1", "C1", 100.0, "SUCCESS"),
    ("P2", "C2", 200.0, "FAILED"),
    ("P3", "C1", 300.0, "SUCCESS"),
    ("P4", "C3", 500.0, "SUCCESS"),
    ("P5", "C2", 150.0, "SUCCESS"),
    ("P6", "C3", 250.0, "SUCCESS"),
    ("P7", "C1", 50.0, "FAILED")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_2")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    payments,
    schema = ["payment_id", "customer_id", "amount", "status"]
)

df.filter(
    col("status") == "SUCCESS"
).groupBy(
    "customer_id"
).agg(
    sum("amount").alias("total_amount"),
    count("payment_id").alias("payment_count"),
).orderBy(
    "total_amount",
    ascending=False
).show()

spark.stop()

