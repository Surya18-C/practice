from pyspark.python.pyspark.shell import spark

df=spark.read.csv('DATASET.csv',header=True)

neg=df.filter(df['label']=='NEGATIVE')
pos=df.filter(df['label']=='POSITIVE')

print("Total Review : ",df.count())
print("Total Positive Reviews : ",pos.count())
print("Total Negitive Reviews : ",neg.count())

if neg.count() > pos.count():
    print("Negitive Review is High")
else:
    print("Positive Review is Hight")