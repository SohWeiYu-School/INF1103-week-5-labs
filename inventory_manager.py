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


def save_inventory():
    print("\nSaving inventory...")
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f"Inventory saved successfully to {INVENTORY_FILE}.")


def display_all():
    print("\nCurrent Inventory")
    print("-" * 48)
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-" * 48)


def add_product():
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock():
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    for item in inventory:
        if item["id"] == product_id:
            print(f"Product Found:\nName: {item['name']}\nCurrent Stock: {item['stock']}")
            item["stock"] = int(input("New Stock Quantity: "))
            print("Stock updated successfully!")
            return
    print("Product not found.")


def search_product():
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    for item in inventory:
        if item["id"] == product_id:
            print("Product Found")
            print("-" * 48)
            print(f"ID: {item['id']}\nName: {item['name']}\nPrice: ${item['price']:.2f}\nStock: {item['stock']}")
            print("-" * 48)
            return
    print("Product not found.")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            search_product()
        elif option == "5":
            save_inventory()
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
