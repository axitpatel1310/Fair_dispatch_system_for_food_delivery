import time
from datetime import datetime
import random

from app.database.connection import SessionLocal
from app.database.models import Order
from app.services.dispatch_service import dispatch_pending_orders
from app.services.delivery_simulation import complete_deliveries


def generate_live_orders(n=5):

    db = SessionLocal()

    for _ in range(n):

        order = Order(
            restaurant_id=random.randint(1, 100),
            latitude=random.uniform(52.45, 52.55),
            longitude=random.uniform(13.30, 13.50),
            zone_id=random.randint(1, 3),
            status="pending"
        )

        db.add(order)

        print(f"New Order Created → {order.restaurant_id}")

    db.commit()
    db.close()


def run_simulation():

    print("Starting Live Delivery Simulation")

    while True:

        print("\n---- SIMULATION STEP ----")

        # create new orders
        if random.random() < 0.6:
            generate_live_orders(random.randint(1,3))

        # assign riders
        dispatch_pending_orders()

        # complete old deliveries
        complete_deliveries()

        print("Cycle complete\n")

        time.sleep(10)


if __name__ == "__main__":
    run_simulation()