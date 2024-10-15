from pyspark.shell import spark
from pyspark.sql.functions import *

data = [("Lap", 25), ("Computer", 30), ("Lap", 30),("Lap",15)]
df = spark.createDataFrame(data, ["name", "age"])

res=df.groupBy("name").agg(count_distinct("age").alias("Total"))

res.show()