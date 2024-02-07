from sqlalchemy import Column, create_engine, String, Integer, ForeignKey
from  sqlalchemy.orm import sessionmaker,declarative_base

Base =declarative_base()
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)

Session=sessionmaker(bind=engine)
session=Session()

class Company(Base):
    __tablename__="company"
    id=Column(Integer,primary_key=True)
    name=Column(String)

class Department(Base):
    __tablename__="department"
    id=Column(Integer,primary_key=True)
    company_id=Column(Integer,ForeignKey('company.id'))
    name=Column(String)

class Employee(Base):
    __tablename__="employee"
    id=Column(Integer,primary_key=True)
    departmetn_id=Column(Integer,ForeignKey('department.id'))
    name=Column(String)
    salary=Column(Integer)
    
Base.metadata.create_all(engine)
company1=Company(name='Netsol 1')   
company2=Company(name='Netsol 2')   
company3=Company(name='Netsol 3')   
company4=Company(name='Netsol 4')

session.add_all(company1,company2,company3,company4)
session.commit()
results=session.query(Employee,Department,Company).select_from(Employee).join(Department).join(Company).all()
for emp,depart,comp in results:
    print(emp.name,depart.name,comp.name)
