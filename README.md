# User Story M1S2

This program is a new version beacuse content options for the user

## What does the program do?

- The program adds products to the inventory along with their price and quantity.
- Validates that the name is not empty or numeric, and that price and quantity are positive numbers.
- show products of the inventory if was added 
- calculte the total of the invetory and the total products in the inventory
- The user decides to exit the program by selecting the last option

## Example usage

When you run the program, you'll see messages like:


### MENU
```text
            Please enter a digit number (1-4) :
            1. Add product
            2. Show producto
            3. Calculate Estadistics
            4. Exit
            Enter →  
```
### ADD PRODUCT
```text
            Enter the name product: cocacola

            Enter the price of the product: 2000

            Enter the quantity: 3
```
### SHOW PRODUCTS
```text
            Product: cocacola | Price: 2000.0 | Quantity: 3
```

### Calculate Statistics
```text
            The total values is: 6000.0
            the Quantity total the produtcs is: 1
```






# User Story M1S1

This program is a simple inventory application written in Python.

## What does the program do?

- Prompts the user for a product name, price, and quantity.
- Validates that the name is not empty or numeric, and that price and quantity are positive numbers.
- Calculates the total cost of the product by multiplying price and quantity.
- Displays the entered data and the total cost on the screen.

## Example usage

When you run the program, you'll see messages like:

```text
welcome to the app!!
Enter the name product: (for example) Apples
Enter the price of the product: 10.5
Enter the quantity: 3

Product: Apples
Price: 10.5
Quantity: 3
Total cost: 31.5
```

## Requirements

- Python 3.8 or higher

## How to run

Open a terminal in the project folder and run:

```bash
python3 inventory.py
```
