from pyspark.shell import spark

from pyspark.sql.functions import *

data=[('Rex','200'),('Babu','100'),('Sam','300')]

schema=['Name','Salary']

df=spark.createDataFrame(data=data,schema=schema)

new_col=df.withColumn('Country',when(col('Salary') > 200 , lit('India')).otherwise('America')) # Add new Column

res=new_col.withColumn('Salary',col('Salary').cast('Integer')) # change data type

new_salary=res.withColumn('Salary',col('Salary')*2) # change value

new_salary.show()
new_salary.printSchema()