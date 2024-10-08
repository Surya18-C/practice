
from pyspark.shell import spark
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

val=[('Rex',20),('Sam',10)]

#val=[{'Name':'Rex' , 'Age':20} , {'Name':'Sam' , 'Age':20} , {'Name':'Babu' , 'Age':20}]

# st=StructType([
#     StructField('Name',StringType()),
#     StructField('Age',IntegerType())
# ])

df=spark.createDataFrame(data=val , schema=['Name','Age'])

df.show()

df.printSchema()