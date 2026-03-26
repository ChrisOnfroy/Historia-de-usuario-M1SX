from services import *
from validations import *
 
#This function, called “menu,” launches the program
def menu():
    isMenu = True
    while isMenu :
        try:
            menu = int(input("""
            Please enter a digit number (1-9) :
            1. Create product
            2. Show Inventory
            3. Search Product
            4. Update Product
            5. Delete Product
            6. Statistics
            7. Upload CSV
            8. Charge CSV
            9. Exit
            Enter →  """))
            validationNum(menu)
            if menu == 1:
                addProduct()
            elif menu == 2:
                showInventory()
            elif menu == 3:
                print("Here you can search product")
            elif menu == 4:
                print("Here you can update product")
            elif menu == 5:
                print("Here you can delete product")
            elif menu == 6:
                calculateStatistics()
            elif menu == 7:
                print("Here you can Upload CSV")
            elif menu == 8:
                print("Here you can charge CSV local")
            elif menu == 9:
                isMenu = False
            else:
                print("")
                print("Enter a valid number")
                
        except ValueError:
            print("")
            print("Cant Enter emptys")
            
            
menu()