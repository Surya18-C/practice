# Databricks notebook source
# MAGIC %md
# MAGIC Help functions

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

from pyspark.sql.functions import *
dbutils_data = spark.read.csv('dbfs:/user1/employee3-1.csv', header=True, inferSchema=True)

dbutils_data.display()


# COMMAND ----------

# MAGIC %md
# MAGIC Data

# COMMAND ----------



dbutils.data.summarize(dbutils_data)

# COMMAND ----------

# MAGIC %md
# MAGIC File system - fs

# COMMAND ----------

dbutils.fs.cp("dbfs:/user1/employee3-1.csv","dbfs:/user1/emp")

# COMMAND ----------

dbutils.fs.head("dbfs:/user1/emp",10)

# COMMAND ----------

dbutils.fs.mv("dbfs:/FileStore/data.csv","dbfs:/user1")

# COMMAND ----------

# MAGIC %md
# MAGIC Notebooks utils -(exit, run)

# COMMAND ----------

name='mythili'
dbutils.notebook.exit('mythu')

# COMMAND ----------

dbutils.notebook.run('/Users/mythilipriya5012@gmail.com//Users/mythilipriya5012@gmail.com/Untitled Notebook 2024-10-24 16:02:59',60)

# COMMAND ----------

# MAGIC %md
# MAGIC Widgets

# COMMAND ----------

# MAGIC %md
# MAGIC Combobox,dropdown,multi-select - similar just change functions

# COMMAND ----------

# dbutils.widgets.help()
dbutils.widgets.combobox(name='fruits',defaultValue='apple',choices=['banana','apple'],label='fruitscup')

# COMMAND ----------

# MAGIC %md
# MAGIC text - same to up but no need to give choices

# COMMAND ----------

dbutils.widgets.text(name='fruitsd',defaultValue='apple',label='fruitsdrop')

# COMMAND ----------

dbutils.widgets.getArgument("fruitsd")


# COMMAND ----------

# MAGIC %md
# MAGIC
