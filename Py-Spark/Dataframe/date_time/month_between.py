from pyspark.shell import spark

from pyspark.sql.functions import *

df=spark.createDataFrame(data=[('2024-05-01','2024-08-10')],schema=['Start','End'])
diff=df.withColumn("diff_Date",months_between(df['end'],df['start']))

diff.show()