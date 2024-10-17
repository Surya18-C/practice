from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

data=[('rex',100,50),('sam',100,60),('ram',200,30)]

df=spark.createDataFrame(data=data,schema=['Name','salary','bonus'])

def add(s,b):
    return s+b

result_udf=udf(add,IntegerType())

res=df.withColumn('Total',result_udf('salary','bonus'))

res.show()