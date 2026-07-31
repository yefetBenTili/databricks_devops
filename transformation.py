from pyspark.sql.functions import col

def read_health_silver_table():
    return spark.read.table("labuser13968342_1785517174.default.health_silver")

def filter_on_income(df, income : int):
    return df.filter(col("income") > income)

def filter_chol(df, chol: str):
    return df.filter(col("HighCholest_Group") == chol)

df = read_health_silver_table()

df_filtred = (df.transform(filter_on_income, income=70000)