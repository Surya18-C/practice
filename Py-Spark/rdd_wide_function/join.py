from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext


rdd1 = sc.parallelize([(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')])

rdd2 = sc.parallelize([(1, 85), (2, 90), (3, 78)])

joined_rdd = rdd1.join(rdd2)

result = joined_rdd.collect()
print(result)
