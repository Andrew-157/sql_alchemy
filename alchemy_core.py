from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+mysqlconnector://root:password@127.0.0.1:3306/users", echo=True)

connection = engine.connect()

connection.execute(text(
    """CREATE TABLE users(
   id INT PRIMARY KEY,
   name VARCHAR(56),
   email VARCHAR(50)
 )
 """
)
)

connection.execute(text(
    """INSERT INTO users (id, name, email) VALUES (:id, :name, :email)"""), [{"id": 1, "name": "Jack", "email": "jack@gmail.com"}])


connection.close()
