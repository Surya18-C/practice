from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext # Creating Spark context

data=[1,2,3,4,5,6]

rdd=sc.parallelize(data)

print(rdd.collect())