from pyspark.python.pyspark.shell import spark

df=spark.read.format('csv').load('../DATASET.csv')

#df.show(truncate=False) # Display All the characters in table

#df.show(truncate=5)         # Display only 5 Character

df.show(vertical=True) # display in vertical format