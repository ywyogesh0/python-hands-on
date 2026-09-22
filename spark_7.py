from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, when

payments = [
    ("P1", 100.0, "success"),
    ("P2", 250.0, "FAILED"),
    ("P3", None, "SUCCESS"),
    ("P4", 500.0, "Success")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_7")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    payments,
    schema = ["payment_id", "amount", "status"]
).withColumn(
    "status", upper(col("status"))
).withColumn(
    "fee",
    when(
        col("status") == "SUCCESS",
        0.02 * col("amount")
    ).otherwise(0.0)
).withColumn(
    "amount_with_fee",
    col("amount") + col("fee")
)

df.show()

spark.stop()

