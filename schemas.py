import datetime as dt
import pydantic 

class BaseContact(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Contact(BaseContact):
    id: int
    date_created: dt.datetime

    class Config:
        orm_mode = True

class CreateContact(BaseContact):
    pass