from datetime import datetime
from app.database.connection import SessionLocal
from app.database.models import RiderMetrics


def update_rider_metrics(rider_id):

    db = SessionLocal()

    current_hour = datetime.now().strftime("%Y-%m-%d %H")

    metric = db.query(RiderMetrics).filter(
        RiderMetrics.rider_id == rider_id,
        RiderMetrics.hour == current_hour
    ).first()

    if metric:

        metric.deliveries_last_hour += 1

    else:

        metric = RiderMetrics(
            rider_id=rider_id,
            hour=current_hour,
            deliveries_last_hour=1,
            weekly_deliveries=1
        )

        db.add(metric)

    db.commit()
    db.close()
    
def get_weekly_deliveries(rider_id):

    db = SessionLocal()

    metrics = db.query(RiderMetrics).filter(
        RiderMetrics.rider_id == rider_id
    ).all()

    total = sum(m.weekly_deliveries for m in metrics)

    db.close()

    return total