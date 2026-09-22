from pyspark.sql import SparkSession


payments = [
    ("P1", ["CARD", "ONLINE"]),
    ("P2", ["BANK_TRANSFER"]),
    ("P3", ["CARD", "INTERNATIONAL", "ONLINE"])
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_9")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

rdd = spark.sparkContext.parallelize(payments)

result = rdd.map(
    lambda p: [(p[0], tag) for tag in p[1]]
).collect()

result_2 = rdd.flatMap(
    lambda p: [(p[0], tag) for tag in p[1]]
).collect()

result_3 = rdd.flatMap(
    lambda p: [(tag, 1) for tag in p[1]]
).reduceByKey(
    lambda p1, p2: p1 + p2
).collect()

print(result)
print(result_2)
print(result_3)

spark.stop()

