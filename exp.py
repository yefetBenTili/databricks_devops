
# this code was pushed from databricks for expirements
df = spark.read.table("labuser13474064_1778591339.default.chol_age_agg")
df = df.filter("Total > 800")
df.display()