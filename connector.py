import mysql.connector 

def connect_new():
    connection = mysql.connector.connect(
        user="root",
        password="MySQLanusayan2011",
        host="local",
        database="scanner"

    )

    return connection

    
