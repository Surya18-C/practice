from pyspark.shell import spark

sc=spark.sparkContext

data=[("Alice", 85), ("Bob", 90), ("Alice", 75), ("Bob", 88), ("Charlie", 92)]

rdd=sc.parallelize(data)


res=rdd.reduceByKey(lambda x,y:x+y)

print(res.collect())