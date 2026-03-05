import time

from app.services.dispatch_service import dispatch_pending_orders
from app.services.delivery_simulation import complete_deliveries


while True:
    dispatch_pending_orders()
    complete_deliveries()
    time.sleep(30)