# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

# Create a Spark session
spark = SparkSession.builder.appName("WindowFunctionRankExample").getOrCreate()

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

# Use rank() window function to assign ranks within each department
df_with_rank = df.withColumn("rank", rank().over(window_spec))

# Show the result
df_with_rank.show()

# Stop the Spark session
spark.stop()
