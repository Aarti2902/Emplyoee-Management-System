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
#connect_db()

def add_employee(name,position,salary):
   query="INSERT INTO employees (name,position,salary) VALUES(%s,%s,%s)"
   conn=connect_db()
   if conn:
      try:
         with conn.cursor() as cursor:
            cursor.execute(query,(name,position,salary))
            conn.commit()
            print("Employee added successfully...")
      except Exception as e:
         print("Error adding employee",e)
      finally:
         conn.close()
add_employee('abc','HR',20000)

