from pyspark.python.pyspark.shell import spark

# find number grater then 25

sc=spark.sparkContext

data=[10, 15, 20, 25, 30, 35, 40, 45, 50]

rdd=sc.parallelize(data)

greater=rdd.filter(lambda x:x>25)

print(greater.collect())