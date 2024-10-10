from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data=[1,2,3]
#creating board cast variable
board_cast=spark.sparkContext(data)

