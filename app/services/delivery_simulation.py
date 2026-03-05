from datetime import datetime, timedelta

from app.database.connection import SessionLocal
from app.database.models import Delivery, Rider


def complete_deliveries():

    db = SessionLocal()

    deliveries = db.query(Delivery).filter(
        Delivery.delivered_time == None
    ).all()

    completed = 0

    for delivery in deliveries:

        assigned = datetime.fromisoformat(delivery.assigned_time)

        # simulate 10 minute delivery
        if datetime.now() - assigned > timedelta(seconds=20):

            delivery.delivered_time = str(datetime.now())
            rider = db.query(Rider).get(delivery.rider_id)
            rider.status = "available"

            completed += 1

    db.commit()
    db.close()

    print(f"{completed} deliveries completed")