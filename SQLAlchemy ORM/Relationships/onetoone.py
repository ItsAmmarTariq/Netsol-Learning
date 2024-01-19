from sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,session
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=True)

Base=declarative_base()



class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    address=relationship('Address',back_populates='user',uselist=False)

class Address(Base):
    __tablename__='addresses'
    id=Column(Integer,primary_key=True)
    email=Column(String,unique=True)
    user_id=Column(Integer,ForeignKey=('users.id'))
    user=relationship('User',back_populates='addresses')

Base.metadata.create_all(engine)


new_user=Users(name='First User')
new_address=Address(email='user@example.com',user=new_user)


# session.add(new_user)
# session.add(new_address)

