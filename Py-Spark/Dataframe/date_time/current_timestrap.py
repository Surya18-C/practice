from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import current_timestamp

df=spark.range(2)

res=df.withColumn('Date',current_timestamp())

res.show(truncate=False)