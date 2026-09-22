from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, TimestampType

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_5")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv(
    "data/payments.csv",
    schema=StructType(
        [
            StructField("payment_id", StringType()),
            StructField("customer_id", StringType()),
            StructField("amount", FloatType()),
            StructField("timestamp", TimestampType()),
            StructField("status", StringType()),
        ]
    )
)

df.filter(
    col("status") == "SUCCESS"
).show()

spark.stop()

