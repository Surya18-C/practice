from pyspark.sql.connect.session import SparkSession

spark=SparkSession.builder.appName('Name').getOrCreate()


