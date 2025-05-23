import pandas as pd
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
    print("File inventory.csv created succesfully\n")
print(df)    

    
print("Statistics:")  
print(f"Amount of products in stock: {len(df)}")
print(f"Total amount of products: {df['Quantity'].sum()}")
df["TotalValue"] = df["Quantity"] * df["Price"]
print(f"Total stock worth: {df['TotalValue'].sum():.2f} ₪\n")

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
    print("Invalid input. Please enter numeric values for ID, quantity, and price.\n")



df["TotalValue"] = df["Quantity"] * df["Price"]
df.to_csv("inventory_updated.csv", index=False)
print("The file 'inventory_updated.csv' was saved successfully.")