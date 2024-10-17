from pyspark.python.pyspark.shell import spark
from pyspark.sql.connect.functions import posexplode

from pyspark.sql.functions import posexplode

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"])
]

df = spark.createDataFrame(data, ["id", "fruits"])
res = df.select("id", posexplode("fruits").alias("pos", "fruit"))

res.show()
