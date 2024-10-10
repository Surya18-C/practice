from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

data1=[(1,'Ram'),(2,'Sam'),(3,'Babu')]

data2=[(1,'M'),(2,'F'),(4,'F')]


rdd1=sc.parallelize(data1)
rdd2=sc.parallelize(data2)

res=rdd1.leftOuterJoin(rdd2)

for x in res.collect():
    print(x)