from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import explode

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"])
]

df = spark.createDataFrame(data, ["id", "fruits"])
res = df.withColumn('fruit_exploded', explode('fruits'))

res.show(truncate=False)
