
from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data=[(' Rex',20),('Babu ',21),('Sam',22)]

df=spark.createDataFrame(data=data , schema=['Name','Age'])

res=df.withColumn('sub_str',substring(df['Name'],2,2))

res.show()