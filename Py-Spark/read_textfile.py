from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

rdd=sc.textFile('DATASET.csv')

print(rdd.collect())