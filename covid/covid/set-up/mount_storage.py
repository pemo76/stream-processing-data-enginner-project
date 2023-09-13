# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "68b15c6b-2161-4b40-a516-571a8043616d",
           "fs.azure.account.oauth2.client.secret": "Z5H8Q~fNNEMLRGiMAWLVLU3iqsJKw26-IWlfCbe.",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/f1fa2bb3-a25c-482f-a57f-3a8c09e09cb1/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covid20reporting20dl.dfs.core.windows.net/",
  mount_point = "/mnt/covid20reporting20dl/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covid20reporting20dl.dfs.core.windows.net/",
  mount_point = "/mnt/covid20reporting20dl/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covid20reporting20dl.dfs.core.windows.net/",
  mount_point = "/mnt/covid20reporting20dl/lookup",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/covid20reporting20dl/lookup"))