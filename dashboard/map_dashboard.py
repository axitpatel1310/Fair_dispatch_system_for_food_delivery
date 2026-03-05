import os
import sqlite3
import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

def load_data():

    DB_PATH = os.path.join(os.path.dirname(__file__), "..", "delivery.db")

    conn = sqlite3.connect(DB_PATH)

    riders = pd.read_sql("SELECT * FROM riders", conn)
    orders = pd.read_sql("SELECT * FROM orders", conn)
    restaurants = pd.read_sql("SELECT * FROM restaurants", conn)
    
    riders["latitude"] = riders["latitude"].astype(float)
    riders["longitude"] = riders["longitude"].astype(float)

    orders["latitude"] = orders["latitude"].astype(float)
    orders["longitude"] = orders["longitude"].astype(float)

    restaurants["latitude"] = restaurants["latitude"].astype(float)
    restaurants["longitude"] = restaurants["longitude"].astype(float)

    conn.close()

    return riders, orders, restaurants

def create_map(riders, orders, restaurants):

    m = folium.Map(location=[52.52, 13.405], zoom_start=12)

    # Restaurants
    for _, r in restaurants.iterrows():

        if pd.isna(r.latitude) or pd.isna(r.longitude):
            continue

        folium.CircleMarker(
            location=[float(r.latitude), float(r.longitude)],
            radius=4,
            color="green",
            fill=True
        ).add_to(m)

    # Riders
    for _, r in riders.iterrows():

        if pd.isna(r.latitude) or pd.isna(r.longitude):
            continue

        color = "blue" if r.status == "available" else "red"

        folium.Marker(
            location=[float(r.latitude), float(r.longitude)],
            icon=folium.Icon(color=color)
        ).add_to(m)

    # Orders (sample only)
    for _, o in orders.head(500).iterrows():

        if o.status != "pending":
            continue

        if pd.isna(o.latitude) or pd.isna(o.longitude):
            continue

        folium.CircleMarker(
            location=[float(o.latitude), float(o.longitude)],
            radius=3,
            color="black",
            fill=True
        ).add_to(m)

    return m

st.title("Food Delivery Dispatch Map")
riders, orders, restaurants = load_data()
st.write("Riders:", len(riders))
st.write("Orders:", len(orders))
st.write("Restaurants:", len(restaurants))
map_object = create_map(riders, orders, restaurants)
st_folium(map_object, width=1000, height=500)