from pyspark.sql import SparkSession


payments = [
    ("P1", "C1", 100.0, "SUCCESS"),
    ("P2", "C2", 200.0, "FAILED"),
    ("P3", "C1", 150.0, "SUCCESS"),
    ("P4", "C3", 300.0, "SUCCESS"),
    ("P5", "C2", 250.0, "SUCCESS")
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_8")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

rdd = spark.sparkContext.parallelize(payments)

result = rdd.filter(
    lambda p: p[3] == "SUCCESS"
).map(
    lambda p: (p[1], p[2])
).reduceByKey(
    lambda x, y: x + y
).collect()

print(result)

spark.stop()

