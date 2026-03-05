import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "delivery.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# reset order statuses
cursor.execute("UPDATE orders SET status='pending'")

# make all riders available
cursor.execute("UPDATE riders SET status='available'")

# clear previous deliveries
cursor.execute("DELETE FROM deliveries")

conn.commit()
conn.close()

print("System reset complete")