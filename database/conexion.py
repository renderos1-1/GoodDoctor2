import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='lcoalhost',
            user='root',
            password='root',
            database='medical_records'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar con MariaDB", e)
        return None
