import sqlite3

conn = sqlite3.connect("delivery.db")
cursor = conn.cursor()
cursor.execute("""
SELECT zone_id, COUNT(*)
FROM orders
GROUP BY zone_id
""")

print(cursor.fetchall())