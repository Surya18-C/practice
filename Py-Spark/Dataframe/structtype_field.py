from pyspark.python.pyspark.shell import spark
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType, ArrayType

data = [("John", 30, 5000, True,[1,2],("Apple",1)),
        ("Sarah", 25, 4000, False,[1,2],("Apple",2)),
        ("Mike", 35, 6000, True , [1,2],("Apple",3))]

desigen=StructType([
StructField("Name",StringType()),
StructField("Age",IntegerType()),
StructField("Salary",IntegerType()),
StructField("IS_Manager",BooleanType()),
StructField("SNO",ArrayType(IntegerType())),
StructField("Detials",StructType([
    StructField("Fruit",StringType()),
    StructField("NO_Of",IntegerType())
]))

])

df=spark.createDataFrame(data=data,schema=desigen)

df.printSchema()

