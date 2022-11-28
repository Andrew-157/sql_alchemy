import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user='root',
                                     password='password', database='users')

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        id INT PRIMARY KEY, 
        name VARCHAR(56), 
        email VARCHAR(50)
        );
    """
)

connection.close()
