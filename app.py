import os
import pymysql

# Database settings from environment variables
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
new_db_name = os.environ['DB_NAME'] # Change as needed
table_name = "sudhar001"  # Change as needed

# Establish a database connection
def connect_to_rds():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Lambda function handler
def lambda_handler(event, context):
    try:
        connection = connect_to_rds()
        with connection.cursor() as cursor:
            # Create a new database
            create_db_sql = f"CREATE DATABASE IF NOT EXISTS {new_db_name};"
            cursor.execute(create_db_sql)

            # Select the new database
            cursor.execute(f"USE {new_db_name};")
