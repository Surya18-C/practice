from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

rdd=sc.parallelize(["I love Spark", "Spark is powerful", "Big data is exciting"])

flt=rdd.filter(lambda word:word.split(" "))

print(flt.collect())