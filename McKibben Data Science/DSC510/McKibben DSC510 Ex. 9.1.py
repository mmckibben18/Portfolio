# DSC510
# Week 9
# Exercise 9.2
# Author: Makayla McKibben
# Date 08.01.2024

# This program takes a user input in order to determine
# what data they would like get from the internet.
# They can select from a Chuck Norris joke, a random fact, or a cat fact.

import json
import requests




def main():
    # Define variable that allows user to
    # indicate their interest in using the program
    option_select = ""
    # User introduction statement
    print("This program will ask you if you would like to get a "
          "Chuck Norris joke and what category of joke you'd like to select. ", end='\n')
    # While loop that asks the user if they'd like to use the program
    while option_select != 'quit':
        print("For a Chuck Norris joke type Norris. "
              "To end the program type Quit at any time. ", end='\n')
        # Gets user input
        option_select = input("What do you want to select? ")
        # Converts user input to lowercase for uniformity
        option_select = option_select.lower()
        # Enters the next section of the program that
        # specifies available categories if user wants
        # a Chuck Norris joke
        if option_select == 'norris':
            cn_category = ""
            # While loop that prints the categories of Chuck Norris jokes
            # available and asks the user for their choice. Repeats until
            # user uses sentinel value "quit"
            while cn_category != 'quit':
                try:
                    # Retrieve categories of Chuck Norris jokes
                    cn_categories = requests.get('https://api.chucknorris.io/jokes/categories')
                    # Prints categories for user by iterating through a for loop
                    print("Categories are: ")
                    for i in range(0, len(cn_categories.json())):
                        print(cn_categories.json()[i], end = '\n')
                    # Request category selection from user
                    print("Please choose a category, spelling must be correct "
                          "or the program will not be able to retrieve the type"
                          " of joke requested.", end = '\n')
                    cn_category = input("Enter the category name or Quit: ")
                    # Converts user input to lowercase so there are
                    # not errors for "Quit" vs. "quit"
                    cn_category = cn_category.lower()
                # Throws specific error if categories could not be retrieved
                except requests.exceptions.HTTPError as errh:
                    print("HTTP Error, API address invalid.", end = '\n')
                    print(errh.args[0])
                    print("Could not retrieve categories. Please try again.", end='\n')
                except requests.exceptions.ReadTimeout as errrt:
                    print("Time out error, server took too long to respond.", end = '\n')
                    print("Could not retrieve categories. Please try again.", end='\n')
                except requests.exceptions.ConnectionError as conerr:
                    print("Connection error, not able to connect to server.", end = '\n')
                    print("Could not retrieve categories. Please try again.", end = '\n')
                except requests.exceptions.RequestException as errex:
                    print("Exception request, non-specific error.", end = '\n')
                    print("Could not retrieve categories. Please try again.", end = '\n')
                # Exits program if user enters quit
                if cn_category == 'quit':
                    exit()
                # Execute program retrieving the category the user wants
                if cn_category != 'quit':
                    try:
                        # For loop iterates through the list of categories which the user
                        # can choose from and identifies if the user input category is
                        # an available option
                        for i in range(0, len(cn_categories.json())):
                            # Tells user they did not enter a valid category and loops again
                            if (i == len(cn_categories.json()) - 1
                                    and cn_category != cn_categories.json()[i]):
                                print("Please check your spelling and select a category.", end = '\n')
                                pass
                            if cn_category == cn_categories.json()[i]:
                                url = "https://api.chucknorris.io/jokes/random"
                                cat_param = {'category': cn_category}
                                # Retrieves and prints the joke from the specified user category
                                # Ends the current loop and asks the user to provide another category
                                # and iterates through the program again
                                try:
                                    chuck_joke = requests.get(url, params = cat_param, timeout=10)
                                    print("The joke is: ", chuck_joke.json()['value'])
                                    break
                                # Throws specific error if categories could not be retrieved
                                except requests.exceptions.HTTPError as errh:
                                    print("HTTP Error, API address invalid.", end='\n')
                                    print(errh.args[0])
                                    print("Could not retrieve categories. Please try again.", end='\n')
                                except requests.exceptions.ReadTimeout as errrt:
                                    print("Time out error, server took too long to respond.", end='\n')
                                    print("Could not retrieve categories. Please try again.", end='\n')
                                except requests.exceptions.ConnectionError as conerr:
                                    print("Connection error, not able to connect to server.", end='\n')
                                    print("Could not retrieve categories. Please try again.", end='\n')
                                except requests.exceptions.RequestException as errex:
                                    print("Exception request, non-specific error.", end='\n')
                                    print("Could not retrieve categories. Please try again.", end='\n')
                            # Increments the for loop if the user input was not a match to the
                            # list indexed value
                            elif i < len(cn_categories.json()):
                                i += 1
                                pass
                    except:
                        print("Could not retrieve jokes. Please try again.")
                        continue
        # Closes the program if user supplies sentinel value
        elif option_select == 'quit':
            exit()
        # Catches spelling errors or nonsensical user entry and loops again
        elif option_select != 'norris' and option_select != 'quit':
            print("Please enter a valid option. ", end = '\n')
            continue
    return

if __name__ == '__main__':
    main()