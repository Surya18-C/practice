
from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data = [("Store1", 5000, 6000, 7000),
        ("Store2", 4500, 5500, 6500),
        ("Store3", 7000, 8000, 9000)]

pivot_df = spark.createDataFrame(data, ["Store", "Jan", "Feb", "Mar"])
res=pivot_df.select('Store',expr("stack(3,'jan',Jan , 'feb' , Feb , 'mar' , Mar) as (Date , Val)"))

res.show()

