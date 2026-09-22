from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, sum, count, expr, to_timestamp, lit
from pyspark.sql.window import Window


payments = [
    ("P1", "C1", 100.0, "SUCCESS", "2026-09-21 10:00:00"),
    ("P1", "C1", 120.0, "SUCCESS", "2026-09-21 10:05:00"),
    ("P2", "C2", 200.0, "FAILED",  "2026-09-21 09:00:00"),
    ("P2", "C2", 250.0, "SUCCESS", "2026-09-21 11:00:00"),
    ("P3", "C1", None,  "SUCCESS", "2026-09-21 12:00:00"),
    ("P4", "C3", 500.0, "SUCCESS", "2026-09-21 08:00:00"),
    ("P5", "C9", 300.0, "SUCCESS", "2026-09-21 13:00:00")
]

customers = [
    ("C1", "Alice", "UK"),
    ("C2", "Bob", "India"),
    ("C3", "Charlie", "UK")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_11")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

pay_df = spark.createDataFrame(
    payments,
    schema = ["payment_id", "customer_id", "amount", "status", "event_timestamp"]
).withColumn(
    "event_timestamp",
    to_timestamp(
        col("event_timestamp"),
        "yyyy-MM-dd HH:mm:ss"
    )
)

cus_df = spark.createDataFrame(
    customers,
    schema = ["customer_id", "customer_name", "country"]
)

# Step 1 — Deduplicate
# Keep the latest event for each payment_id using row_number() ordered by event_timestamp descending.

window_spec = Window.partitionBy("payment_id").orderBy(col("event_timestamp").desc())

dedup_df = pay_df.withColumn(
    "row_number",
    row_number().over(window_spec)
).filter(
    col("row_number") == 1
).drop("row_number")

# Step 2 — Validate
# Keep only records where status == "SUCCESS", amount is non-null and greater than zero, and customer_id is non-null.

val_df = dedup_df.filter(
    (col("status") == "SUCCESS") &
    (col("amount").isNotNull()) &
    (col("amount") > 0.0) &
    (col("customer_id").isNotNull())
)

# Step 3 — Enrich
# Join the valid payments to the customer reference DataFrame. Use an inner join so payments without a matching customer are excluded from this reporting output.

join_df = val_df.join(
    cus_df,
    "customer_id",
    "inner"
)

# Step 4 — Aggregate
# Group by customer_id, customer_name and country. Calculate total_amount and payment_count.

agg_df = join_df.groupBy(
    "customer_id",
    "customer_name",
    "country"
).agg(
    sum("amount").alias("total_amount"),
    count(expr("*")).alias("payment_count")
)

# Step 5 — Write
# Add a processing_date column with the value 2026-09-21, then write the result as Parquet partitioned by processing_date.

import tempfile
with tempfile.TemporaryDirectory(prefix="payments_") as output_path:
    agg_df.withColumn(
        "processing_date",
        lit("2026-09-21")
    ).write.partitionBy("processing_date").mode("overwrite").parquet(output_path)

    spark.read.parquet(output_path).show()

# completed

spark.stop()

