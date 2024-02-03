from faker import Faker
from sqlalchemy.orm import Session

from database import SessionLocal
from models import UserTable

# Create a Faker instance
fake = Faker()

db = SessionLocal()


def seed_db(db: Session):
    for _ in range(50):  # Create 50 fake users
        new_user = UserTable(
            username=fake.unique.user_name(),
            name=fake.name(),
            age=fake.random_int(min=18, max=90, step=1),
            gender=fake.random_element(elements=("M", "F")),
            phone=fake.phone_number(),
            country=fake.country(),
        )
        db.add(new_user)
    db.commit()


seed_db(db)
