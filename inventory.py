import pandas as pd

# Load File or create a new one
try:
    df = pd.read_csv("inventory.csv")
    print("File found and loaded\n")
except FileNotFoundError:
    print("File not found, creating a new one now\n")
    inventory = {
        "ProductID": [101, 102, 103, 104],
        "Name": ["Keyboard", "Mouse", "Monitor", "USB-C Cable"],
        "Quantity": [10, 25, 5, 100],
        "Price": [99.90, 49.90, 799.00, 19.90]
    }
    df = pd.DataFrame(inventory)
    df.to_csv("inventory.csv", index=False)
    print("File inventory.csv created successfully\n")

# Functions

def show_inventory():
    print("\nCurrent Inventory:")
    print(df)

def show_stats():
    print("\nStatistics:")
    print(f"Amount of products in stock: {len(df)}")
    print(f"Total amount of products: {df['Quantity'].sum()}")
    df["TotalValue"] = df["Quantity"] * df["Price"]
    print(f"Total stock worth: {df['TotalValue'].sum():.2f} ₪")

def search_product():
    try:
        product_id = int(input("Enter ProductID to search: "))
        product = df[df["ProductID"] == product_id]
        if not product.empty:
            print("Product found:")
            print(product)
        else:
            print("Product not found.\n")
    except ValueError:
        print("Please enter numbers only.\n")

def update_quantity():
    try:
        update_id = int(input("Enter ProductID to update quantity: "))
        if update_id in df["ProductID"].values:
            new_qty = int(input("Enter the new quantity: "))
            df.loc[df["ProductID"] == update_id, "Quantity"] = new_qty
            print("Quantity updated successfully.\n")
        else:
            print("Product does not exist.\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def add_product():
    global df  # <- esto va al principio, antes de usar df
    try:
        print("Add a new product:\n")
        new_id = int(input("Enter new ProductID: "))
        if new_id in df["ProductID"].values:
            print("A product with this ID already exists.\n")
        else:
            new_name = input("Enter product name: ")
            new_qty = int(input("Enter quantity: "))
            new_price = float(input("Enter price: "))
            new_row = pd.DataFrame([{
                "ProductID": new_id,
                "Name": new_name,
                "Quantity": new_qty,
                "Price": new_price
            }])
            df = pd.concat([df, new_row], ignore_index=True)
            print("Product added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")

def low_stock():
    print("\nProducts with quantity lower than 10:")
    print(df[df["Quantity"] < 10])

def save_and_exit():
    df["TotalValue"] = df["Quantity"] * df["Price"]
    df.to_csv("inventory_updated.csv", index=False)
    df.to_excel("inventory_summary.xlsx", index=False)
    print("\nInventory saved to 'inventory_updated.csv' and 'inventory_summary.xlsx'. Goodbye!")
    exit()

# Intereactive Menu

while True:
    print("\nMenu:")
    print("1. View Inventory")
    print("2. Inventory Stats")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Add Product")
    print("6. Show Low Stock")
    print("7. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        show_stats()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_quantity()
    elif choice == "5":
        add_product()
    elif choice == "6":
        low_stock()
    elif choice == "7":
        save_and_exit()
    else:
        print("Invalid option. Please try again.")
