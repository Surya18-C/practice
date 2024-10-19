from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType

# Create a Spark session
spark = SparkSession.builder.appName("JSON Handling Example").getOrCreate()

# Define the schema for the JSON file (Optional, but useful for performance)
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("address", StructType([
        StructField("city", StringType(), True),
        StructField("zipcode", StringType(), True)
    ]), True),
    StructField("friends", ArrayType(StringType()), True)
])

# Reading a JSON file with the defined schema
df = spark.read.schema(schema).json("/path/to/input/json_file.json")

# Show the DataFrame
print("Original DataFrame:")
df.show(truncate=False)

# Print the schema of the DataFrame
print("Schema of the DataFrame:")
df.printSchema()

# Select specific fields (including nested fields)
df_selected = df.select("name", "age", "address.city", "address.zipcode")
print("Selected fields (including nested fields):")
df_selected.show(truncate=False)

# Explode the "friends" array (if it exists) to flatten the array values
df_exploded = df.withColumn("friend", explode(col("friends")))
print("Exploded 'friends' array into individual rows:")
df_exploded.select("name", "friend").show(truncate=False)

# Filter rows based on a condition
df_filtered = df.filter(col("age") > 25)
print("Rows where age is greater than 25:")
df_filtered.show(truncate=False)

# Write the manipulated DataFrame to a new JSON file
output_path = "/path/to/output/json_file"
df_exploded.write.json(output_path)

# Stop the Spark session
spark.stop()
