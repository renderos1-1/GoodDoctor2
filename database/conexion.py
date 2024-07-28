import mariadb
from mariadb import Error

def create_connection():
    try:
        connection = mariadb.connect(
            host='localhost',
            user='root',
            password='root',
            database='medical_records'
        )
        if connection:
            print("Connected to MariaDB")
            return connection
    except Error as e:
        print("Error connecting to MariaDB:", e)
        return None
