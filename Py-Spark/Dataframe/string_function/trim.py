from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data=[(' Rex',20),('Babu ',21),('Sam',22)]

df=spark.createDataFrame(data=data , schema=['Name','Age'])

res=df.withColumn('New_Name',trim(df['Name'])) # Trim Only removes leading space

res.show()