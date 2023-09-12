from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app import models

from app.database import get_db, Base
from app.models import Person
from .main import app

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:okite.com@localhost/crud_test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Persons = [Person(name= "Okite Chimaobi"), Person(name = "Chimaobi"), Person(name = "Samuel")]

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    

def test_get_person(client, session):
    session.add_all(Persons)
    session.commit()
    #test getting Person by ID
    response = client.get("/api/1")
    assert response.status_code == 200

    #test dynamically getting person by name
    response = client.get("/api?name=Chimaobi")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Chimaobi"

    #test getting none registered users
    response = client.get("/api/5")
    assert response.status_code == 404, response.text

def test_create_person_by_json(client):
    response = client.post("/api", json={"name": "Chimaobi Okite"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Chimaobi Okite"

def test_create_person_by_name(client):
    response = client.post("/api?name=Okite")
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Okite"

def test_update_person_by_name(client):
    client.post("/api?name=Okite")
    response = client.put("/api?name=Okite", json={"name": "Chimaobi Okite"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Chimaobi Okite"

def test_update_person_by_id(client):
    person = client.post("/api?name=Okite")
    person = person.json()
    user_id = person['user_id']
    response = client.put(f"/api/{user_id}", json={"name": "Chimaobi Okite"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Chimaobi Okite"

def test_delete_person_by_name(client):
    client.post("/api?name=Okite")
    response = client.delete("/api?name=Okite")
    assert response.status_code == 204

def test_update_person_by_id(client):
    person = client.post("/api?name=Okite")
    person = person.json()
    user_id = person['user_id']
    response = client.delete(f"/api/{user_id}")
    assert response.status_code == 204
