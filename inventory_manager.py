"""
INF1103 Week 5 - Inventory Management System
"""

import json
import os

INVENTORY_FILE = "inventory.json"

# Initial inventory with 3 products
inventory = [
    {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00,   "stock": 25},
]


def load_inventory():
    global inventory
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        with open(INVENTORY_FILE, "r") as f:
            inventory = json.load(f)
        print("Inventory loaded successfully.")
    else:
        print(f"{INVENTORY_FILE} not found. Starting with default inventory.")


def display_all():
    print("\nCurrent Inventory")
    print("-" * 48)
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-" * 48)
