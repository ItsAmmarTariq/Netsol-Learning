from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base  # Import declarative_base directly

# Replace the placeholders with your PostgreSQL connection details
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    cnic = Column(Integer)
    grade = Column(String(50))
    print('im in class getting executing')


Base.metadata.create_all(engine)

    

# student1 = Student(name='Joe Root', age=40,cnic=3450214953585,grade='cnic grade')
# # # student2 = Student(name='Ali Haider', age=22, grade='B')

# # # # Add the instances to the session
# session.add(student1)
# # # session.add(student2)

# # # # Commit the session to persist the changes to the database
# session.commit()

# # # # Close the session
# session.close()




# # check if the data is inserted
# # Create a new session for querying
# new_session = Session()

# # Query all records from the "student" table
# students = new_session.query(Student).all()

# # Print the queried data
# for student in students:
#     print(student)
#     # print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

# # Close the new session
# new_session.close()

