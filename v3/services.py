from validations import *
from functions import *
import csv as csv

inventory = []



#The `addproduct` feature allows us to add products and save them in a dictionary stored in a list.
def addProduct():
    
    #These whiles help us ensure that, as long as the condition is true, the user must enter the correct information.
    validateProduct = True
    while validateProduct:
        print("")
        nameProduct = input("Enter the name product: ").strip()
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
    
    with open("inventory.csv", mode="a", newline='', encoding='utf-8') as archive:
        
        writer = csv.writer(archive)
        
        # Verificar si el archivo está vacío para escribir el encabezado
        archive.seek(0, 2)  
        if archive.tell() == 0: 
            writer.writerow(["name", "price", "quantity"])

        data = list(product.items())
        
        # Escribir el nuevo producto
        writer.writerow([data[0][1], data[1][1], data[2][1]])
            
        print(f"Product '{nameProduct}' added successfully!")

#This feature helps us show the user all the products stored in inventory.
def showInventory():
    with open("inventory.csv", mode="r") as archive:
        print("")
        lines = archive.readlines()

        for i, line in enumerate(lines[1:], 1):  # Saltar encabezado
            data = line.strip().split(',')
            if len(data) >= 3:
                nombre = data[0]
                precio = float(data[1])
                cantidad = int(data[2])
                    
                print(f"{i:<4} {nombre:<25} ${precio:<11.2f} {cantidad:<10}")
        

        
        
#This feature helps us calculate all the data for each product and how many there are.
def calculateStatistics():
    totalValuesInventory = 0
    
    #This loop allows us to calculate the total inventory.
    for i, product in enumerate(inventory):
        data = list(product.items())
        totalValuesInventory += calculateTotalProduct(data[1][1], data[2][1])
        i += 1

    print(f"""
    The total values is: {totalValuesInventory}
    the Quantity total the produtcs is: {i}
    """)
    