from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rider(Base):

    __tablename__ = "riders"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    zone_id = Column(Integer)
    status = Column(String)
    rider_type = Column(String)

class Restaurant(Base):

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    zone_id = Column(Integer)

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    latitude = Column(Float)
    longitude = Column(Float)
    zone_id = Column(Integer)
    status = Column(String)

class Delivery(Base):

    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    rider_id = Column(Integer)
    assigned_time = Column(String)
    delivered_time = Column(String)


class RiderMetrics(Base):

    __tablename__ = "rider_metrics"

    id = Column(Integer, primary_key=True)
    rider_id = Column(Integer)
    hour = Column(String)
    deliveries_last_hour = Column(Integer)
    weekly_deliveries = Column(Integer)