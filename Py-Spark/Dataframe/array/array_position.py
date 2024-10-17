from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import array_position

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"])
]

df = spark.createDataFrame(data, ["id", "fruits"])

res=df.withColumn("Array_Position",array_position('fruits','apple'))

res.show()
