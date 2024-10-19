from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data = [("1234567891234567",),
        ("5678912345671234",),
        ("9123456712345678",),
        ("1234567812341122",),
        ("1234567812341342",)]

columns=["card_number"]

credit_card_df = spark.createDataFrame(data, columns)

def mask_card_number(card_number):
    return "*" *(len(card_number)-4)+card_number[-4:]

cus_udf=udf(mask_card_number , StringType())

res=credit_card_df.withColumn('Result',cus_udf('card_number'))

res.show()