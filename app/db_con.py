import psycopg2

DB_HOST = 'localhost'
DB_USERNAME = 'waracci'
DB_PASS = 'root'
DB_NAME = 'test_database_workshop'
DB_PORT = 5432

url = "dbname='test_database_workshop' host='localhost'\
                 port='5432' user='waracci' password='root'"

# Creating the connection
con = psycopg2.connect(url)
# Creating the cursor
cur = con.cursor()

# Executing the SQL query
result = con.execute()

# Closing the connection
con.close()
