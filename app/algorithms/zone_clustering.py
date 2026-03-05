import pandas as pd
from sklearn.cluster import KMeans


def create_zones(order_data):

    coords = order_data[["latitude", "longitude"]]

    model = KMeans(n_clusters=3, random_state=42)

    order_data["zone"] = model.fit_predict(coords)

    return order_data, model