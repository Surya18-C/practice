# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank

# Create a Spark session
spark = SparkSession.builder.appName("WindowFunctionDenseRankExample").getOrCreate()

# Sample data: Employee information with departments
data = [
    ('John', 'HR', 5000),
    ('Alice', 'HR', 6000),
    ('Bob', 'HR', 5000),
    ('Cathy', 'Finance', 7000),
    ('Alex', 'Finance', 7500),
    ('David', 'Finance', 7000)
]

# Create a DataFrame from the sample data
columns = ["Name", "Department", "Salary"]
df = spark.createDataFrame(data, columns)

# Define a window specification
window_spec = Window.partitionBy("Department").orderBy("Salary")

# Use dense_rank() window function to assign dense ranks within each department
df_with_dense_rank = df.withColumn("dense_rank", dense_rank().over(window_spec))

# Show the result
df_with_dense_rank.show()

# Stop the Spark session
spark.stop()
