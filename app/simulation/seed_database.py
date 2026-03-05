from .generate_restaurants import generate_restaurants
from .generate_riders import generate_riders
from .generate_orders import generate_orders

def seed():

    generate_restaurants(100)
    generate_riders(50)
    generate_orders(10000)

if __name__ == "__main__":
    seed()