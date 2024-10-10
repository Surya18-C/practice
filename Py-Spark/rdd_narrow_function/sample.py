from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data=[1,2,3,4,5]

rdd=sc.parallelize(data)

res=rdd.sample(True , 0.6)

print(res.collect())