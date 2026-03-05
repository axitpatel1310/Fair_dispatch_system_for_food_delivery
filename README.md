# Fair Dispatch System for Food Delivery Riders

## Overview

The **Fair Dispatch System for Food Delivery Riders** is a logistics simulation platform designed to model how modern food delivery companies assign orders to delivery riders.
The system simulates **order generation, rider dispatching, delivery completion, and live geospatial visualization**.

The goal of the project is to explore **data-driven dispatch optimization**, **fair workload distribution**, and **logistics simulation** using Python.

This project demonstrates how delivery platforms can balance:

* delivery efficiency
* rider workload fairness
* operational visibility

through a modular backend architecture.

---

# Key Features

## 1. Fair Dispatch Algorithm

Orders are assigned to riders using a fairness-based dispatch rule.

The system prioritizes riders who have completed **fewer deliveries in the current hour**, ensuring balanced workload distribution.

Dispatch priority factors:

* rider availability
* deliveries completed in the last hour
* zone demand

---

## 2. Zone-Based Demand Clustering

Historical order data is analyzed to create **delivery zones** based on demand density.

Zones help optimize dispatch decisions by identifying areas with:

* high order demand
* medium demand
* low demand

Clustering is implemented using **K-Means geographic clustering**.

---

## 3. Real-Time Simulation

The system continuously simulates a food delivery environment:

1. New orders appear periodically.
2. The dispatch engine assigns riders.
3. Deliveries complete after a simulated time interval.
4. Riders become available again for new assignments.

This creates a **continuous logistics simulation loop**.

---

## 4. Live Geospatial Dashboard

A Streamlit dashboard visualizes the system on a map.

The map displays:

* restaurants
* delivery riders
* pending orders

Marker colors:

| Marker | Meaning          |
| ------ | ---------------- |
| Green  | Restaurants      |
| Blue   | Available riders |
| Red    | Busy riders      |
| Black  | Pending orders   |

The dashboard allows monitoring of **dispatch activity across the city**.

---

# System Architecture

```
Order Generator
      │
      ▼
Zone Detection
      │
      ▼
Dispatch Algorithm
      │
      ▼
Delivery Assignment
      │
      ▼
Delivery Completion Simulation
      │
      ▼
Map Visualization Dashboard
```

---

# Project Structure

```
Project
│
├── app
│   ├── algorithms
│   │     dispatch_algorithm.py
│   │     zone_clustering.py
│   │
│   ├── database
│   │     connection.py
│   │     models.py
│   │     init_db.py
│   │
│   ├── services
│   │     dispatch_service.py
│   │     delivery_simulation.py
│   │     rider_metrics_service.py
│   │
│   ├── simulation
│   │     generate_orders.py
│   │     generate_riders.py
│   │     generate_restaurants.py
│   │     live_simulation.py
│   │
│   └── utils
│         reset_system.py
│
├── dashboard
│     map_dashboard.py
│
├── delivery.db
└── README.md
```

---

# Technology Stack

| Component            | Technology   |
| -------------------- | ------------ |
| Programming Language | Python       |
| Database             | SQLite       |
| Data Processing      | Pandas       |
| Machine Learning     | Scikit-Learn |
| Visualization        | Folium       |
| Dashboard            | Streamlit    |

---

# Installation

## 1. Clone the repository

```
git clone <repository-url>
cd fair-dispatch-system
```

---

## 2. Install dependencies

```
pip install pandas numpy sqlalchemy scikit-learn folium streamlit streamlit-folium
```

---

## 3. Initialize the database

```
python -m app.database.init_db
```

---

## 4. Seed the system with simulated data

```
python -m app.simulation.seed_database
```

This generates:

* restaurants
* riders
* historical orders

---

# Running the Simulation

## Start the live logistics simulation

```
python -m app.simulation.live_simulation
```

This continuously:

* generates new orders
* assigns riders
* completes deliveries

---

## Launch the dashboard

```
streamlit run dashboard/map_dashboard.py
```

Open in browser:

```
http://localhost:8501
```

---

# Example Dispatch Output

```
---- SIMULATION STEP ----

New Order Created → 72
New Order Created → 41

Dispatch: Order 103 → Rider 8
Dispatch: Order 104 → Rider 4

2 deliveries completed
Cycle complete
```

---

# Future Improvements

The current system focuses on **fair workload distribution**. Future improvements may include:

### Distance-Based Dispatch Optimization

Improve rider selection using a multi-factor scoring function:

```
dispatch_score =
0.5 × distance
0.3 × workload fairness
0.2 × rider idle time
```

---

### Route Visualization

Draw real delivery routes on the map:

```
Restaurant → Rider → Customer
```

---

### Reinforcement Learning Dispatch

Train a reinforcement learning agent to optimize:

* delivery time
* rider utilization
* operational cost

---

# Educational Value

This project demonstrates several real-world concepts used in delivery platforms:

* logistics optimization
* geospatial clustering
* dispatch algorithms
* simulation systems
* operational dashboards

It provides a simplified model of systems used by large-scale food delivery platforms.

---

# License

This project is intended for educational and research purposes.
