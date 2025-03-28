from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

spark = SparkSession.builder.appName("SalesDataETL").getOrCreate()

raw_data_path = "abfss://container@datalake.dfs.core.windows.net/raw/sales_data.csv"
df = spark.read.csv(raw_data_path, header=True, inferSchema=True)

df_cleaned = (df.dropna()
    .withColumn("total_price", expr("quantity * price"))
    .withColumn("order_date", col("order_date").cast("date")))

processed_data_path = "abfss://container@datalake.dfs.core.windows.net/processed/sales_data.parquet"
df_cleaned.write.mode("overwrite").parquet(processed_data_path)

spark.stop()
