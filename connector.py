import mysql.connector 

def connect_new():
    connection = mysql.connector.connect(
        user="root",
        password="your_password",
        host="local",
        database="scanner"

    )

    return connection

    
