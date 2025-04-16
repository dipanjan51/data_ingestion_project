import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node airport dim
airportdim_node1744642287244 = glueContext.create_dynamic_frame.from_catalog(database="airline_datamart", table_name="dev_airlines_airports_dim", redshift_tmp_dir="s3://temp-s3-dataa/airline_dim/", transformation_ctx="airportdim_node1744642287244")

# Script generated for node daily_flights_data
daily_flights_data_node1744645534157 = glueContext.create_dynamic_frame.from_catalog(database="airline_datamart", table_name="raw_daily_flights", transformation_ctx="daily_flights_data_node1744645534157")

# Script generated for node Filter
Filter_node1744649860342 = Filter.apply(frame=daily_flights_data_node1744645534157, f=lambda row: (row["depdelay"] >= 60), transformation_ctx="Filter_node1744649860342")

# Script generated for node join_depart_airport
Filter_node1744649860342DF = Filter_node1744649860342.toDF()
airportdim_node1744642287244DF = airportdim_node1744642287244.toDF()
join_depart_airport_node1744660979287 = DynamicFrame.fromDF(Filter_node1744649860342DF.join(airportdim_node1744642287244DF, (Filter_node1744649860342DF['originairportid'] == airportdim_node1744642287244DF['airport_id']), "left"), glueContext, "join_depart_airport_node1744660979287")

# Script generated for node modify_dep_airport_column
modify_dep_airport_column_node1744661419259 = ApplyMapping.apply(frame=join_depart_airport_node1744660979287, mappings=[("carrier", "string", "carrier", "varchar"), ("destairportid", "long", "destairportid", "long"), ("depdelay", "long", "dep_delay", "bigint"), ("arrdelay", "long", "arr_delay", "bigint"), ("city", "string", "dep_city", "varchar"), ("name", "string", "dep_airport", "varchar"), ("state", "string", "dep_state", "varchar")], transformation_ctx="modify_dep_airport_column_node1744661419259")

# Script generated for node join_arr_airport
modify_dep_airport_column_node1744661419259DF = modify_dep_airport_column_node1744661419259.toDF()
airportdim_node1744642287244DF = airportdim_node1744642287244.toDF()
join_arr_airport_node1744662019470 = DynamicFrame.fromDF(modify_dep_airport_column_node1744661419259DF.join(airportdim_node1744642287244DF, (modify_dep_airport_column_node1744661419259DF['destairportid'] == airportdim_node1744642287244DF['airport_id']), "left"), glueContext, "join_arr_airport_node1744662019470")

# Script generated for node modify_arr_airport_column
modify_arr_airport_column_node1744662376156 = ApplyMapping.apply(frame=join_arr_airport_node1744662019470, mappings=[("carrier", "varchar", "carrier", "string"), ("dep_state", "varchar", "dep_state", "string"), ("state", "string", "arr_state", "string"), ("arr_delay", "bigint", "arr_delay", "long"), ("city", "string", "arr_city", "string"), ("name", "string", "arr_airport", "string"), ("dep_city", "varchar", "dep_city", "string"), ("dep_delay", "bigint", "dep_delay", "long"), ("dep_airport", "varchar", "dep_airport", "string")], transformation_ctx="modify_arr_airport_column_node1744662376156")

# Script generated for node redshift_target_table
redshift_target_table_node1744663164047 = glueContext.write_dynamic_frame.from_catalog(frame=modify_arr_airport_column_node1744662376156, database="airline_datamart", table_name="dev_airlines_daily_flights_fact", redshift_tmp_dir="s3://temp-s3-dataa/airline_fact/",additional_options={"aws_iam_role": "arn:aws:iam::111349184842:role/redshift_role"}, transformation_ctx="redshift_target_table_node1744663164047")

job.commit()
