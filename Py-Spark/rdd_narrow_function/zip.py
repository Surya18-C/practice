from pyspark.shell import spark

sc=spark.sparkContext

data1 = [1, 2, 3,4,5]
data2 = ['a', 'b', 'c']

rdd1 = sc.parallelize(data1)
rdd2 = sc.parallelize(data2)

zip_rdd=rdd1.zip(rdd2)

print(zip_rdd.collect())