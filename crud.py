from sqlalchemy import Column, Integer, String, create_engine, select, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base 


engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))



def add_new():
    new_student=student(name='Khadija 2',age=33,grade='A+')
    session.add(new_student)
    session.commit()

def fetch_data():
    query=select(student.id,student.name,student.age,student.grade).order_by(student.id)
    result=session.execute(query)
    for row in result:
        print(row.id,row.name,row.age,row.grade)

def update_data(id,updated_grade):
    check=session.query(student).filter_by(id=id).first()
    if check:
        query_update=update(student).where(student.id==id).values(grade=updated_grade)
        session.execute(query_update)
        session.commit()
    else:
        print('No student is found related to provided id')

def delete_data(student_id):

    student_del=session.query(student).filter_by(id=student_id).first()
    if student_del:
         session.delete(student_del)
         session.commit()
         print('Record is deleted successfully')

    else:
        print(f'no student is found with the id: {student_id}')
    


    

# update_data(342,'grade')
# add_new()


fetch_data()
delete_data(8)
fetch_data()

session.close()


session.delete()


