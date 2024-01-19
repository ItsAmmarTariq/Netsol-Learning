from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)


Base=declarative_base()

class Customers(Base):
    __tablename__='customers'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    address=Column(String)
    email=Column(String)

# Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()

# adding objects into database

'''
instance=Customers(name='Ammar Tariq',address='anarkali lahore',email='ammarch935@gmail.com')
session.add(instance)
session.commit()

'''

res=session.query(Customers).all()


for row in res:
    print('Name : ',row.name,'Adress : ',row.address,'Email : ',row.email)


