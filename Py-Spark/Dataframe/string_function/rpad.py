
from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data=[(' Rex',20),('Babu ',21),('Sam',22)]

df=spark.createDataFrame(data=data , schema=['Name','Age'])

res=df.withColumn('Name',lpad(df['Name'],6,'$'))

res.show()