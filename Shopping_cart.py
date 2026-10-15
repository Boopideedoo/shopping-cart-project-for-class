#Name: Your name
#Date: Current Date
#Purpose: Create an online shopping cart program

#TODO: ItemToPurchase class

#TODO: ShoppingCart class

#TODO: print_menu function

#TODO: implement menus in execute_menu()

def execute_menu(menuOp, theCart):
    if menuOp == 'a':
        print('under construction')


    elif menuOp == 'r':
        print('under construction')


    elif menuOp == 'c':
        print('under construction')


    elif menuOp == 'o':
        print('under construction')

                
if __name__ == "__main__":
    menu_choice = ' '
    #TODO: Prompt user for name and date


    my_cart = ShoppingCart(cust_name, day_date)

    print_menu()

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')
        if menu_choice in ['a', 'r', 'c', 'o']:
            execute_menu(menu_choice, my_cart)
            print_menu()
