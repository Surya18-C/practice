# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date, current_timestamp, date_format, datediff, add_months, year, month, dayofmonth

# Create a Spark session
spark = SparkSession.builder.appName("DateTimeFunctionExample").getOrCreate()

# Sample data: Employee information with hire dates
data = [
    ('John', '2023-01-10'),
    ('Alice', '2022-06-25'),
    ('Bob', '2021-03-15')
]

# Create a DataFrame from the sample data
columns = ["Name", "HireDate"]
df = spark.createDataFrame(data, columns)

# Convert the 'HireDate' column to DateType
df = df.withColumn("HireDate", df["HireDate"].cast("date"))

# Add columns for various date and time functions
df_with_date = df.withColumn("CurrentDate", current_date()) \
                 .withColumn("CurrentTimestamp", current_timestamp()) \
                 .withColumn("FormattedDate", date_format(df["HireDate"], "dd/MM/yyyy")) \
                 .withColumn("DaysSinceHire", datediff(current_date(), df["HireDate"])) \
                 .withColumn("NextHireAnniversary", add_months(df["HireDate"], 12)) \
                 .withColumn("HireYear", year(df["HireDate"])) \
                 .withColumn("HireMonth", month(df["HireDate"])) \
                 .withColumn("HireDay", dayofmonth(df["HireDate"]))

# Show the result
df_with_date.show(truncate=False)

# Stop the Spark session
spark.stop()
