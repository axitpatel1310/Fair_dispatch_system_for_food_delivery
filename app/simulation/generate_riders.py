import random
from app.database.connection import SessionLocal
from app.database.models import Rider

db = SessionLocal()

def generate_riders(n=50):

    for i in range(n):

        rider = Rider(
            name=f"Rider_{i}",
            latitude=random.uniform(52.45, 52.55),
            longitude=random.uniform(13.30, 13.50),
            zone_id=random.randint(1,3),
            status="available",
            rider_type=random.choice(["part_time","full_time"])
        )

        db.add(rider)

    db.commit()
    db.close()

    print(f"{n} riders created")