import mysql.connector

# Establishing the connection
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Harsha@01',
    auth_plugin='mysql_native_password'  # Specify the authentication plugin
)

# Preparing a cursor object
cursorObject = dataBase.cursor()

# Creating a database
cursorObject.execute("CREATE DATABASE pjango")

print("All Done!")
