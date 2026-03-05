from datetime import datetime

from app.database.connection import SessionLocal
from app.database.models import Order, Rider, Delivery, RiderMetrics
from app.algorithms.dispatch_algorithm import select_rider
from app.services.rider_metrics_service import update_rider_metrics


def dispatch_pending_orders():

    db = SessionLocal()

    orders = db.query(Order).filter(Order.status == "pending").limit(10).all()

    riders = db.query(Rider).all()

    # Build metrics dictionary
    metrics = {}

    rider_metrics = db.query(RiderMetrics).all()

    for m in rider_metrics:
        metrics[m.rider_id] = m.deliveries_last_hour

    assignments = 0
    print("Pending orders:", len(orders))
    print("Available riders:", len([r for r in riders if r.status=="available"]))
    for order in orders:

        rider = select_rider(order.zone_id, riders, metrics)

        if rider is None:
            continue
        
        metrics[rider.id] = metrics.get(rider.id, 0) + 1

        delivery = Delivery(
            order_id=order.id,
            rider_id=rider.id,
            assigned_time=str(datetime.now())
        )
        print(
           f"Order {order.id} assigned to Rider {rider.id} in Zone {order.zone_id}"
        )

        order.status = "assigned"

        rider.status = "busy"

        update_rider_metrics(rider.id)

        db.add(delivery)

        assignments += 1

    db.commit()
    db.close()

    print(f"{assignments} orders assigned")