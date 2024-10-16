
from pyspark.python.pyspark.shell import spark
from pyspark.sql import Window
from pyspark.sql.functions import window, row_number

data = [
     ("Bob", "English", 80),
    ("Alice", "Math", 95),
    ("Bob", "Math", 85),
     ("Sam", "Math", 85),
    ("Alice", "English", 90),
    ("Charlie", "Math", 95),
    ("Charlie", "English", 70)
]

# Create DataFrame
df = spark.createDataFrame(data, ["student", "subject", "score"])

win=Window.partitionBy('subject').orderBy('score')

res=df.withColumn("SNO",row_number().over(win))

res.show()