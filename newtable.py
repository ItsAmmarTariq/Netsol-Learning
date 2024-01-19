from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   email = Column(String)
   cnic = Column(String)
   role= Column(String)

Base.metadata.create_all(engine)




def add_employee(name,email,cnic,role):
    from sqlalchemy.orm import sessionmaker

    Session=sessionmaker(bind=engine)
    session=Session()

    instance=Employee(name=name,email=email,cnic=cnic,role=role)
    session.add(instance)
    session.commit()
    print('Emplooye successfully added')

def show_employee():
    from sqlalchemy.orm import sessionmaker
    Session=sessionmaker(bind=engine)
    session=Session()
    result=session.query(Employee).all()
    
    for row in result:
        print('Name : ',row.name, 'Email : ',row.email,'Role : ',row.role)



print('Select 1 for adding Employee. \n 2 for show all the employee \n 3 for delete employee \n 4 for update the current employee')
opt=input('What you want to do ? ')

if opt =='1':
    print('enter the details of the employee')
    emp_name=input('enter employee name : ')
    emp_email=input('enter the email : ')
    emp_cnic=input('enter the cnic : ')
    emp_role=input('enter the employee role : ')
    add_employee(emp_name,emp_email,emp_cnic,emp_role)

    

elif opt=='2':
    show_employee()

elif opt=='3':
    pass

elif opt=='4':
    pass

else:
    print('you entered the wrong choice')

