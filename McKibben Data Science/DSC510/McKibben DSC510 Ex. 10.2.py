# Makayla McKibben
# DSC510
# Week 10
# Programming Assignment 10.2

import locale


def main():
    # Create an empty list to hold all the prices
    # of the items added in the cash register
    price = []

    # Create the cash register class
    class CashRegister:
        itemCount = 0

        # Create method that prints statement letting
        # you know you're creating a cash register
        def __init__(self):
            print("You're creating a "
                  "cash register to track your purchases.")

        # Create add_item method that tallies the number
        # of items and tracks all the prices in a list
        def add_item(self, item_price):
            price.append(item_price)
            CashRegister.itemCount += 1

        # Getter method for count of items
        @property
        def get_count(self):
            return CashRegister.itemCount

        # Getter method for total cost of items
        @property
        def get_total(self):
            return sum(price)

    # Print welcome message for user
    print("This program will track your items and "
          "give you the total number of items and "
          "the total cost when you exit.", end = '\n')

    # Try statement that errors if you do not provide
    # confirmation you'd like to use the program
    # or quit. This try statement lets the user enter
    # the while loop that will try to confirm they want
    # to use the program
    try:
        use_prog = ""
        # The while loop that takes in user value indicating
        # if they'd like to use the program. Quit is the sentinel value
        while use_prog != 'quit':
            use_prog = input(
            "Would you like to use this program? "
            "If so enter Yes otherwise enter Quit "
            "at any time to stop running the program: ")
            # Converts the user input so there aren't case errors
            use_prog = use_prog.lower()
            # If/else statements that move the user to the next while loop
            if use_prog == "yes":
                break
            # Closes the program if user supplies sentinel value
            elif use_prog == 'quit':
                exit()
            # Catches spelling errors or nonsensical user entry and loops again
            elif use_prog != 'yes' and use_prog != 'quit':
                print("Please enter a valid option. ", end='\n')
                continue
    except ValueError:
        print("Please enter Yes otherwise enter Quit")
        pass
    # Initializes the cash register
    cash_register = CashRegister()
    # While loop that takes item inputs, quit is the sentinel value
    while use_prog != 'quit':
        # Takes user input of price, provides error if incorrect
        # data type, closes and provides output data if provided sentinel value
        if use_prog == 'yes' or use_prog == 'y':
            try:
                item_price = input("Enter item price: ")
                try:
                    item_price = float(item_price)
                    cash_register.add_item(item_price)
                    pass
                except ValueError:
                    item_price = item_price.lower()
                    if item_price == 'quit':
                        break
                    else:
                        print("Please try again, enter a valid price or quit. ", end='\n')
                        use_prog = 'yes'
                        continue
                # Try statement that restarts the loop if user wants to continue
                # using the program. Exits and prints output data if user is done
                try:
                    use_prog = input("Continue using program? Type Y, Yes, or Quit: ")
                    use_prog = use_prog.lower()
                    if use_prog == 'y':
                        continue
                        # Closes the program if user supplies sentinel value
                    elif use_prog == 'quit':
                        break
                    # Catches spelling errors or nonsensical user entry and loops again
                    elif (use_prog != 'yes' or use_prog != 'y') and use_prog != 'quit':
                        print("Please try again, enter a valid price or quit. ", end='\n')
                        use_prog = 'yes'
                        continue
                except ValueError:
                    print("Invalid input. Enter Y or Quit")
            except ValueError:
                print("Please enter a number")
                continue
    # Turns the total price into currency format
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
    total_price = locale.currency(cash_register.get_total, grouping=True)
    # Prints output data from all items
    print("Number of items: ", cash_register.get_count, ", Total of items: ", total_price)
    return


if __name__ == '__main__':
    main()