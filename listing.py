import database
import pprint 
from api import apiRequest
from database import add_orders, get_orders, create_table

def get_item_info():
    # user input
    item_name = input("Enter Item Name: ")
    order_type = input("Enter order type (buy/sell): ")

    # Convert item name to lowercase,spaces to underscores, 
    # and removes trailing underscores
    item_name = item_name.lower()
    item_name = item_name.replace(" ", "_")
    while item_name.endswith("_"):
        item_name = item_name[:-1]

    # Check if table for the item exists
    create_table(item_name)

    # Retrieve orders from API and add to database
    orders = apiRequest(item_name)
    if orders:
        # process or output the retrieved data
        print(f"Successfully retrieved {len(orders)} orders for {item_name}.")
        add_orders(item_name, orders)
    else:
        print("Failed to retrieve orders.")

    # Retrieve orders from database for given item and order_type
    orders = database.get_orders(item_name, order_type)

    return orders

# Get item info and retrieve orders
orders = get_item_info()

# Output orders
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(orders)
