from functions import *
from validations import *
 
#This function, called “menu,” launches the program
def menu():
    isMenu = True
    while isMenu :
        try:
            menu = int(input("""
            Please enter a digit number (1-4) :
            1. Add product
            2. Show product
            3. Calculate statistics
            4. Exit
            Enter →  """))
            validationNum(menu)
            if menu == 1:
                addProduct()
            elif menu == 2:
                showInventory()
            elif menu == 3:
                calculateStatistics()
            elif menu == 4:
                isMenu = False
            else:
                print("")
                print("Enter a valid number")
                
        except ValueError:
            print("")
            print("Cant Enter emptys")
            
            
menu()