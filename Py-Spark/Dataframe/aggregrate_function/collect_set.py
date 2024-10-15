from pyspark.shell import spark
from pyspark.sql.functions import *

data = [("Lap", 25), ("Computer", 30), ("Lap", 30),("Lap",15)]
df = spark.createDataFrame(data, ["name", "age"])

res=df.agg(collect_set("age"))

res.show()