from pyspark.python.pyspark.shell import spark

df=spark.read.format('csv').option('header',True).load(path='DATASET.csv')

#df=spark.read.csv(path='DATASET.csv',header=True,inferSchema=True)

df.show(100)

