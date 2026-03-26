from validations import *
from functions import *

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

#This feature helps us show the user all the products stored in inventory.
def showInventory():
    
    #This loop allows us to access the items in the inventory, add them to a list, and then print each one
    for product in inventory:
        data = list(product.items())
        print("")
        print(f"Product: {data[0][1]} | Price: {data[1][1]} | Quantity: {data[2][1]}")
        
        
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
    