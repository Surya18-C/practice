from pyspark.python.pyspark.shell import spark
from pyspark.sql.types import *
from pyspark.sql.functions import *

purchase_data = [
    (1, "iphone13"),
    (1, "dell i5 core"),
    (2, "iphone13"),
    (2, "dell i5 core"),
    (3, "iphone13"),
    (3, "dell i5 core"),
    (1, "dell i3 core"),
    (1, "hp i5 core"),
    (1, "iphone14"),
    (3, "iphone14"),
    (4, "iphone13")
]
purchase_schema = StructType([
    StructField("customer", IntegerType(), True),
    StructField("product_model", StringType(), True)
])


purchase_data_df = spark.createDataFrame(purchase_data, schema=purchase_schema)

grouped_purchase_df = purchase_data_df.groupBy("customer").agg(collect_set('product_model'))
filtered_data=grouped_purchase_df.filter(col('customer')==4)

filtered_data.show(truncate=False)