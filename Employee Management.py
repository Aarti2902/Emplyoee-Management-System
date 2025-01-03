import psycopg2

# database connectivity

DB_CONFIG = {
    "dbname":"employeedb",
    "user":"postgres",
    "password":"123",
    "host":"localhost",
    "port":5432

}

def connect_db():
     """Connect to the postgreSQL database"""
     try:
        conn=psycopg2.connect(**DB_CONFIG)
        print("Connection Succesful to database")
        return conn
     except Exception as e:
        print("Error connecting to database",e)
        return None
connect_db()