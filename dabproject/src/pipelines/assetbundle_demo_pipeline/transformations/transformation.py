import dlt
@dlt.table 
def tranformed():
    return spark.range(10)