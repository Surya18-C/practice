from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data=[('apple',1),('orange',2),('apple',3)]

rdd=sc.parallelize(data)

res=rdd.groupBy()

format_list=[(key,list(value))for key , value in res.collect()]

print(format_list)