from pyspark.sql import SparkSession


payments = [
    ("C1", 100.0),
    ("C1", 200.0),
    ("C2", 50.0),
    ("C2", 150.0),
    ("C2", 250.0)
]

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("spark_10")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

rdd = spark.sparkContext.parallelize(payments)

# Accumulator: (sum, count)
seqFunc = (lambda acc, amount, : (acc[0] + amount, acc[1] + 1))
combFunc = (lambda acc_1, acc_2, : (acc_1[0] + acc_2[0], acc_1[1] + acc_2[1]))

result = rdd.aggregateByKey(
    (0.0, 0),
    seqFunc,
    combFunc
).mapValues(lambda acc: acc[0] / acc[1]).collect()

print(result)

spark.stop()

