import csv
from services import inventory

# Nombre del archivo donde se guardarán los datos
FILENAME = "v3/data/inventory.csv"

def save_inventory():

    try:
        with open(FILENAME, 'a', newline='', encoding='utf-8') as file:

            fieldnames = ['name', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            

            writer.writeheader()

            for product in inventory:
                writer.writerow(product)
        
        print("\n Inventory saved successfully to '{FILENAME}'")
        return True
    
    except:
        print("\n Error saving inventory")
        return False

def load_inventory():
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            
            reader = csv.DictReader(file)
            
            for row in reader:
                product = {
                    'name': row['name'].strip().lower(),
                    'price': float(row['price']),
                    'quantity': int(row['quantity'])
                }
                inventory.append(product)
                
        return inventory
    
    except FileNotFoundError:
        print("\n File not found. Starting empty.")
        return inventory
    except:
        print("\n Error loading: ")
        return inventory