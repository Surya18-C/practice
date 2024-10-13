from pyspark.shell import spark

from pyspark.sql.functions import *

data = [("John", "HR", 3000),
        ("Sarah", "Finance", 4500),
        ("Mike", "Finance", 4000),
        ("Sam", "HR", 3500),
        ("Anna", "IT", 5000),
        ("James", "IT", 5500)]

columns = ["Name", "Department", "Salary"]

df=spark.createDataFrame(data,columns)

res=df.groupBy("Department").agg(
    avg("Salary").alias("AverageSalary"),
    sum("Salary").alias("TotalSalary"),
    max("Salary").alias("Max_Salary"),
)

finial_res=res.orderBy(res['Max_Salary'].desc())

finial_res.show()
