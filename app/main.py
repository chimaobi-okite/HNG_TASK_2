from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import exc
from typing import List, Optional

from .database import engine, get_db
from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api", response_model=schemas.PersonOut, status_code=201)
def create_person(name: str = None, person: schemas.Person = None,db: Session = Depends(get_db)):

    if name:
        new_person = models.Person(name = name)
    elif person:
        new_person = models.Person(**person.model_dump())
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail=f"Add details")
    try:
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
    except exc.IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail=f"Person with name {person.name} already exists")

    return new_person

@app.get("/api/{user_id}", response_model=schemas.PersonOut)
def get_person(user_id:int, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.user_id == user_id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    return person

@app.put("/api/{user_id}", response_model=schemas.PersonOut, status_code=201)
def update_person(user_id: int, new_person: schemas.Person,db: Session = Depends(get_db)):

    person_query = db.query(models.Person).filter(models.Person.user_id == user_id)
    old_person = person_query.first()
    if not old_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    try:
        person_query.update(new_person.model_dump(), synchronize_session=False)
        db.commit()
        db.refresh(person_query.first())
    except exc.IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail=f"Person with name {new_person.name} already exists")
    return person_query.first()

@app.delete("/api/{user_id}",  status_code=204)
def delete_person(user_id: int,db: Session = Depends(get_db)):

    person_query = db.query(models.Person).filter(models.Person.user_id == user_id)
    old_person = person_query.first()
    if not old_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    person_query.delete(synchronize_session=False)
    db.commit()
    return 

@app.get("/api", response_model=schemas.PersonOut)
def get_person(name:str, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.name == name).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    return person

@app.put("/api", response_model=schemas.PersonOut, status_code=201)
def update_person(name: str, new_person: schemas.Person, db: Session = Depends(get_db)):

    old_person = db.query(models.Person).filter(models.Person.name == name).first()
    if not old_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    person_query = db.query(models.Person).filter(models.Person.user_id == old_person.user_id)
    try:
        person_query.update(new_person.model_dump(), synchronize_session=False)
        db.commit()
        db.refresh(person_query.first())
    except exc.IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail=f"Person with name {new_person.name} already exists")
    return person_query.first()

@app.delete("/api",  status_code=204)
def delete_person(name:str,db: Session = Depends(get_db)):

    person_query = db.query(models.Person).filter(models.Person.name == name)
    old_person = person_query.first()
    if not old_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="person not found")
    person_query.delete(synchronize_session=False)
    db.commit()
    return 

# @app.post("/api", response_model=schemas.PersonOut, status_code=201)
# def create_person(name: str ,db: Session = Depends(get_db)):

#     new_person = models.Person(name = name)
#     try:
#         db.add(new_person)
#         db.commit()
#         db.refresh(new_person)
#     except exc.IntegrityError as e:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                              detail=f"Person with name {name} already exists")

#     return new_person