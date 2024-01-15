# reading data from the database

from sqlalchemy import create_engine,text
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)

connection=engine.connect()


try:
    query=text('SELECT * FROM student')
    result=connection.execute(query)

    for row in result:
        print(row.id,row.name,row.age,row.grade)
except Exception as e:
    print('Error :',e)

finally:
    connection.close()


from sqlalchemy import create_engine,text
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)