from typing import Union

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db.mealmentor_database import SessionLocal, engine
from models.models import Base, UserTable

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users", tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserTable).all()
    return {"users": users}
