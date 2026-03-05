import random
from app.database.connection import SessionLocal
from app.database.models import Restaurant

db = SessionLocal()

def generate_restaurants(n=100):

    for i in range(n):

        restaurant = Restaurant(
            name=f"Restaurant_{i}",
            latitude=random.uniform(52.45, 52.55),
            longitude=random.uniform(13.30, 13.50),
            zone_id=random.randint(1,3)
        )

        db.add(restaurant)

    db.commit()
    db.close()

    print(f"{n} restaurants created")