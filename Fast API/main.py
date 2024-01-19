from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    # id: int
    firstname: str
    lastname: str
    isMale: bool


@app.get('/', response_model=list[Person], status_code=status.HTTP_200_OK)
def getAll_Person():
    getAll = db.query(models.Person).all()
    return getAll


@app.post('/addPerson', response_model=Person, status_code=status.HTTP_201_CREATED)
def add_Person(person: Person):
    newPerson = models.Person(
        # id=person.id,
        firstname=person.firstname,
        lastname=person.lastname,
        isMale=person.isMale
    )
    findPerson=db.query(models.Person).filter(models.Person.id==person.id)
    if findPerson:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="person with this id already exists")

    else:
        db.add(newPerson)
        db.commit()
        return newPerson



@app.put('/updatePerson/{person_id}',response_model=Person,status_code=status.HTTP_201_CREATED)
def updatePerson(person_id:int,person:Person):
    find_Person=db.query(models.Person).filter(models.Person.id==person_id).first()
    if find_Person is not None:
        find_Person.firstname=person.firstname
        find_Person.lastname=person.lastname
        find_Person.isMale=person.isMale

        db.commit()
        return find_Person
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no person is found with id {person_id}")


@app.delete('/deletePerson/{person_id}',response_model=Person,status_code=status.HTTP_302_FOUND)
def deletePerson(person_id:int):
    del_person=db.query(models.Person).filter(models.Person.id==person_id).first()
    if del_person is not None:
        db.delete(del_person)
        db.commit()
    else:
        raise HTTPException(status_code=404,detail="person with the id is not found")

    return deletePerson



