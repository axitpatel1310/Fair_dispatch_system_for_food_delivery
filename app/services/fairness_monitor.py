from app.database.connection import SessionLocal
from app.database.models import RiderMetrics


def check_hourly_targets():

    db = SessionLocal()

    metrics = db.query(RiderMetrics).all()

    for m in metrics:

        if m.deliveries_last_hour < 2:

            print(
                f"Rider {m.rider_id} below hourly target"
            )

    db.close()