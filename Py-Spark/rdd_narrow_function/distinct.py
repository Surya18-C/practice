from pyspark.shell import spark

sc=spark.sparkContext

data = [1, 2, 2, 3, 4, 4, 5, 6, 6]

rdd=sc.parallelize(data)

res=rdd.distinct()

print(res.collect())