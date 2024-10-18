from pyspark.python.pyspark.shell import spark

data = [("Store1", "Jan", 5000),
        ("Store1", "Feb", 6000),
        ("Store1", "Mar", 7000),
        ("Store2", "Jan", 4500),
        ("Store2", "Feb", 5500),
        ("Store2", "Mar", 6500),
        ("Store3", "Jan", 7000),
        ("Store3", "Feb", 8000),
        ("Store3", "Mar", 9000)]

# Create DataFrame
df = spark.createDataFrame(data, ["Store", "Month", "Sales"])

df_pivot=df.groupBy('Store').pivot('Month').sum('Sales')

df_pivot.show()