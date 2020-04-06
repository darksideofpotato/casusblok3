import mysql.connector
from mysql.connector import Error

class Dal:
    pass


##testje voor database connectie
try:
    connection = mysql.connector.connect(
      host="localhost",
      database='casus_voorraden',
      user="root",
      passwd="root", auth_plugin='mysql_native_password'
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("Database is closed")
