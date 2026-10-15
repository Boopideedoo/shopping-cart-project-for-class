# shopping-cart-project-for-class
This project is a shopping cart task for my class

I will post instructions here incase anyone else tries to do the same project since this repository will be public

In this project you will build an online shopping cart. The shopping cart will have two classes: ItemToPurchase and ShoppingCart. You will have the ability to add, modify, and remove items in your shopping cart. After you purchase all of your items, you can display the total cost of the cart. 

Step 1: Create the ItemToPurchase class 
(1) Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor 
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()

Ex. of print_item_cost() output:

Bottled Water 10 @ $1 = $10




Step 2: Build the ShoppingCart class with the following data attributes and related methods.
Parameterized constructor which takes the customer name and date as parameters 
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2025"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has a parameter of type ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output a message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's quantity. Has a parameter of type ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, modify item in cart.
If item cannot be found (by name) in cart, output a message: Item not found in cart. Nothing modified.
print_total()
Outputs total of objects in cart.
If cart is empty, output a message: SHOPPING CART IS EMPTY
Ex. of print_total() output:

John Doe's Shopping Cart - February 1, 2025
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521


Step 3: In the main section of the code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart. 
Ex:

Enter customer's name:
John Doe
Enter today's date:
February 1, 2025

Customer name: John Doe
Today's date: February 1, 2025
Step 4: Implement the print_menu() function
print_menu()
Prints the following menu of options to manipulate the shopping cart. 
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
o - Output shopping cart
q - Quit
Step 5: Implement the menu options in execute_menu(). These options are currently stubs.
Step 5a: In the main section of the code, when print_menu() is called, the user is prompted for their choice of menu options. Each option is represented by a single character.

If an invalid character is entered, the code continues to prompt for a valid choice. When a valid option is entered,  execute_menu()is called. This continues until the user enters 'q'. 

Hint: Implement Quit before implementing other options. They can be implemented in any order.

Ex:

a - Add item to cart
r - Remove item from cart
c - Change item quantity
o - Output shopping cart
q - Quit

Choose an option:
Step 5b: Implement "o - Output shopping cart" menu option in execute_menu(). 

Ex:

OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2025
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521


Step 5c: Implement "a - Add item to cart" menu option in execute_menu(). 

Ex:

ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item price:
189
Enter the item quantity:
2
Step 5d: Implement "r - Remove item from cart" menu option in execute_menu(). 

Ex:

REMOVE ITEM FROM CART
Enter name of item to remove:
Chocolate Chips
Step 5e: Implement "c - Change item quantity" menu option in execute_menu(). 

Hint: Make a new ItemToPurchase object before using ModifyItem() method.

Ex:

CHANGE ITEM QUANTITY
Enter the item name:
Nike Romaleos
Enter the new quantity:
3
Test your code with multiple items, add new items, remove an item, modify an item, then display the shopping cart. Debug any issues you have and submit your project. 
