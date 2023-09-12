from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    name :str

class PersonOut(Person):
    user_id: int

    class ConfigDict:
        from_attributes = True
