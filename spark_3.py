from pyspark.sql.functions import broadcast
from pyspark.sql import SparkSession


customers = [
    ("C1", "Alice", "London"),
    ("C2", "Bob", "Manchester"),
    ("C3", "Charlie", "Birmingham"),
    ("C4", "David", "Leeds")
]

payments = [
    ("P1", "C1", 100.0),
    ("P2", "C2", 200.0),
    ("P3", "C1", 300.0),
    ("P4", "C3", 500.0),
    ("P5", "C5", 250.0)
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_3")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

cus_df = spark.createDataFrame(
    customers,
    schema = ["customer_id", "customer_name", "city"]
)

pay_df = spark.createDataFrame(
    payments,
    schema = ["payment_id", "customer_id", "amount"]
)

pay_df.join(
    broadcast(cus_df),
    "customer_id",
    "left"
).select(
    "payment_id",
    "customer_id",
    "amount",
    "customer_name",
    "city"
).show()

spark.stop()

