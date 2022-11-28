from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+mysqlconnector://root:password@127.0.0.1:3306/users", echo=True, future=True)


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

connection.commit()

connection.close()
