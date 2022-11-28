from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

engine = create_engine(
    "mysql+mysqlconnector://root:password@127.0.0.1:3306/users", echo=True)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(56))
              )

contacts = Table('contacts', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('user_id', None, ForeignKey('users.id')),
                 Column('email', String(50))
                 )

metadata.create_all(engine)

insert_1 = users.insert().values(id=1, name="Donald")
print(insert_1)

insert_2 = users.insert().values(id=2, name="Arnold")
insert_3 = users.insert().values(id=3, name="Lizzy")

connection = engine.connect()
connection.execute(insert_1)
connection.execute(insert_2)
connection.execute(insert_3)

select_query = select(users)
result = connection.execute(select_query)

for row in result:
    print(row)

connection.close()
