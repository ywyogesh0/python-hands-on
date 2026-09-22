from pyspark.sql import SparkSession
from pyspark.sql.functions import col

payments = [
    ("P1", "C1", 100.0, "SUCCESS"),
    ("P2", None, 200.0, "SUCCESS"),
    ("P3", "C1", None, "SUCCESS"),
    ("P4", "C3", 500.0, None),
    ("P5", "C2", 300.0, "FAILED"),
    ("P6", "C4", 400.0, "SUCCESS")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_1")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    payments,
    schema=["payment_id", "customer_id", "amount", "status"]
)

df.printSchema()

# using pyspark.sql.functions - col function
df.filter(
    col("customer_id").isNotNull() &
    col("amount").isNotNull() &
    (col("status") == "SUCCESS")
).select(
    col("payment_id"),
    col("customer_id"),
    col("amount")
).withColumn(
    "fee",
    0.02 * col("amount")
).na.drop(
    subset=["payment_id"]
).show()

# using SQL expression
df.filter(
    "customer_id IS NOT NULL AND amount IS NOT NULL AND status = 'SUCCESS'"
).select(
    col("payment_id"),
    col("customer_id"),
    col("amount")
).withColumn(
    "fee",
    0.02 * col("amount")
).na.drop(
    subset=["payment_id"]
).show()

spark.stop()
