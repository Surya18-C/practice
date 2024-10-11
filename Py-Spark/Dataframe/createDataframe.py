from pyspark.python.pyspark.shell import spark

df=spark.createDataFrame(data=[('rex',20),('sam',30),('babu',30)] , schema=['Name','Age'])

df.show()

