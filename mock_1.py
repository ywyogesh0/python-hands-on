# Requirements: Implement using pyspark that selects the highest-version event for each payment,
# excludes events that are not successful or have an invalid amount,
# and returns the total successful amount per customer. The function must not mutate the input.

# For this exercise, an amount is valid if it is a positive integer or float;
# None, zero, negative values and booleans are invalid.
# Assume payment_id, customer_id, status and version are present,
# and versions are integers with a unique highest version per payment.

# expected result: {"C1": 120, "C3": 300}

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, sum
from pyspark.sql.window import Window


payments = [
    {"payment_id": "P1", "customer_id": "C1", "amount": 100, "status": "SUCCESS", "version": 1},
    {"payment_id": "P1", "customer_id": "C1", "amount": 120, "status": "SUCCESS", "version": 2},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200, "status": "SUCCESS", "version": 1},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200, "status": "FAILED",  "version": 2},
    {"payment_id": "P3", "customer_id": "C1", "amount": None, "status": "SUCCESS", "version": 1},
    {"payment_id": "P4", "customer_id": "C3", "amount": 300, "status": "SUCCESS", "version": 1}
]

spark = SparkSession.builder.master("local[*]").appName("mock_1").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.createDataFrame(
    payments
)

window_spec = Window.partitionBy("payment_id").orderBy(col("version").desc())

result = df.withColumn(
    "rn",
    row_number().over(window_spec)
).filter(
    col("rn") == 1
).drop(
    "rn"
).filter(
    (col("amount").isNotNull()) &
    (col("amount") > 0) &
    (col("status") == "SUCCESS")
).groupBy(
    "customer_id"
).agg(
    sum("amount").alias("total_successful_amount")
).collect()

r_dict = {}

for r in result:
    r_dict[r[0]] = r[1]

print(r_dict)

spark.stop()