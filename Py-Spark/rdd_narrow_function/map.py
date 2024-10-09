from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data=['apple','banana','orange']

rdd=sc.parallelize(data)

up=rdd.map(lambda word : word.upper())

print(up.collect())