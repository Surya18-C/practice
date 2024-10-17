from pyspark.python.pyspark.shell import spark
from pyspark.sql.connect.functions import col
from pyspark.sql.functions import current_date, month

df=spark.range(2)
add=df.withColumn('current_month',month(current_date()))

add.show()