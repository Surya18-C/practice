from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data=[
    (1,"Apple","Banana"),
    (2,"Pinaple","Stabuary"),
    (3,"carrot","orange"),
]
df=spark.createDataFrame(data=data,schema=['id','fruit1','fruit2'])
res=df.withColumn('Result',array("fruit1","fruit2"))

res.show()