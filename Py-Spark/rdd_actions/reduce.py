from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data=[1,2,3,4,5]

rdd=sc.parallelize(data)

res=rdd.reduce(lambda x,y : x+y)

print(res)