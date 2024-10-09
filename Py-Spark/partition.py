from pyspark.shell import spark

sc=spark.sparkContext

data=[1,2,3,4,5]

rdd=sc.parallelize(data,6)



print(rdd.getNumPartitions())

print(rdd.glom().collect()) # collect values from all partitions glom