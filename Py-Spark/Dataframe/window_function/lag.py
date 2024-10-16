from pyspark.python.pyspark.shell import spark
from pyspark.sql.connect.functions import lead
from pyspark.sql.connect.window import Window
from pyspark.sql.functions import lag

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

res=df.withColumn("lag",lag("score").over(Window.partitionBy("subject").orderBy("score")))

res.show()