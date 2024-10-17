from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

df = spark.createDataFrame(data=[(1,), (2,)], schema=['Id'])

res = df.withColumn('currentDate', current_date())

change_format = res.withColumn('formatedDate', date_format(res.currentDate, 'dd,MM,yyyy'))

add_datef = change_format.withColumn('resultDate', to_date(change_format.currentDate, 'dd,MM,yyyy'))

add_datef.show()
add_datef.printSchema()
