spark.read\
  .option("header", "true")\
  .csv("/databricks-datasets/definitive-guide/data/retail-data/all/online-retail-dataset.csv")\
  .repartition(2)\
  .selectExpr("instr(Description, 'GLASS') >= 1 as is_glass")\
  .groupBy("is_glass")\
  .count()\
  .collect()


# COMMAND ----------

