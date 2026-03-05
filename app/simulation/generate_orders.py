import random
from app.database.connection import SessionLocal
from app.database.models import Order

db = SessionLocal()

def generate_orders(n=10000):

    for i in range(n):

        order = Order(
            restaurant_id=random.randint(1,100),
            latitude=random.uniform(52.45,52.55),
            longitude=random.uniform(13.30,13.50),
            zone_id=random.randint(1,3),
            status="pending"
        )

        db.add(order)

    db.commit()
    db.close()

    print(f"{n} orders created")