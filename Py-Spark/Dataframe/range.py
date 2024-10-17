from pyspark.shell import spark

df=spark.range(2)

df.show()