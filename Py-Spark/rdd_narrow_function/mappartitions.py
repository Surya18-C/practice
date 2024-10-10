from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import xpath

sc=spark.sparkContext

data=[1,2,3,4,5,6,7,8,9]

rdd=sc.parallelize(data,3)

def add(x):
    return (x+1 for x in data)

aad=rdd.mapPartitions(add)

print(aad.collect())

