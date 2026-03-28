from validations import *
from functions import *

inventory = []

#The `addproduct` feature allows us to add products and save them in a dictionary stored in a list.
def addProduct():
    
    #These whiles help us ensure that, as long as the condition is true, the user must enter the correct information.
    validateProduct = True
    while validateProduct:
        print("")
        nameProduct = input("Enter the name product: ").strip().lower()
        validateProduct = validationProductName(nameProduct)       
        
    validatePrice = True  
    while validatePrice:
        try:
            print("")
            price = float(input("Enter the price of the product: "))
            validatePrice = validationNum(price)

        except ValueError:
            print("Error: please enter a valide number")

    validateQuantity = True
    while validateQuantity:
        try:
            print("")
            quantity = int(input("Enter the quantity: "))
            validateQuantity = validationNum(quantity)
            
        except ValueError:
            print("Error: please enter a valide number")
            
    product = { "name" : nameProduct,
                "price" : price,
                "quantity" : quantity
               }
    
    inventory.append(product)
    


#This feature helps us show the user all the products stored in inventory.
def showInventory():
    
    
    #This loop allows us to access the items in the inventory, add them to a list, and then print each one
    for product in inventory:
        data = list(product.items())
        print("")
        print(f"Product: {data[0][1]} | Price: {data[1][1]} | Quantity: {data[2][1]}")
        
def searchProduct():
    search = input("Enter name product: ").lower().strip()
    exist = False

    for product in inventory:
        if product["name"] == search:
            print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
            exist = True
            return True  # Retornar True si se encontró
    
    if not exist:
        print("Product name not found.")
        return False  # Retornar False si no se encontró

def UpdateProduct():
    
    search = input("Enter name product: ").lower().strip()
    exist = False

    for product in inventory:
        if product["name"] == search:  # Acceso directo al diccionario
            print(f"\nCurrent product: {product['name']} - ${product['price']} - {product['quantity']} units")
            
            # Obtener nuevos valores con validaciones similares a addProduct()
            new_name = input("Write new name: ").strip().lower()
            new_price = float(input("Write new price: "))
            new_quantity = int(input("Write new quantity: "))
            
            # Actualizar el diccionario original
            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity
            
            exist = True
            print("Product updated successfully!")
            return True  # Retornar True indicando éxito
    
    if not exist:
        print("Product name not found.")
        return False

    
def deleteProduct():
    search = input("Enter name product to delete: ").lower().strip()
    exist = False

    for i, product in enumerate(inventory):
        if product["name"] == search:
            print(f"\nProduct found: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
            
            confirm = input("Are you sure you want to delete this product? (y/n): ").lower().strip()
            
            if confirm == 'y':
                deleted = inventory.pop(i)
                print(f"\nProduct '{deleted['name']}' has been deleted successfully!")
                return True
            else:
                print("Deletion cancelled.")
                return False
    
    if not exist:
        print("Product name not found.")
        return False
#This feature helps us calculate all the data for each product and how many there are.
def calculateStatistics():
    
    print("\n" + "="*50)
    print("INVENTORY STATISTICS")
    print("="*50)
    
    if not inventory:
        print("Inventory is empty. No statistics available.")
        return False

    unidades_totales = sum(product["quantity"] for product in inventory)
    
    valor_total = sum(product["price"] * product["quantity"] for product in inventory)

    producto_mas_caro = max(inventory, key=lambda x: x["price"])
    
    producto_mayor_stock = max(inventory, key=lambda x: x["quantity"])
    
    # Mostrar resultados
    print(f"\n TOTAL UNITS: {unidades_totales} units")
    print(f" TOTAL VALUE: ${valor_total}")
    print(f"\n MOST EXPENSIVE PRODUCT:")
    print(f"   • Name: {producto_mas_caro['name']}")
    print(f"   • Price: ${producto_mas_caro['price']}")
    print(f"\n HIGHEST STOCK PRODUCT:")
    print(f"   • Name: {producto_mayor_stock['name']}")
    print(f"   • Quantity: {producto_mayor_stock['quantity']} units")
    
    return True
    