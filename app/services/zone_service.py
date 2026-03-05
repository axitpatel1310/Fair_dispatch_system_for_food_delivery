import pandas as pd

from app.database.connection import SessionLocal
from app.database.models import Order
from app.algorithms.zone_clustering import create_zones


def compute_zones():

    db = SessionLocal()

    orders = db.query(Order).all()

    data = []

    for o in orders:

        data.append({
            "id": o.id,
            "latitude": o.latitude,
            "longitude": o.longitude
        })

    df = pd.DataFrame(data)

    df, model = create_zones(df)

    for _, row in df.iterrows():

        order = db.query(Order).get(row["id"])

        order.zone_id = int(row["zone"]) + 1

    db.commit()
    db.close()

    print("Zones assigned to orders")