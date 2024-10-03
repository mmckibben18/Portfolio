# DSC510
# Week 5
# Exercise 6.1
# Author: Makayla McKibben
# Date 07.09.2024

temperatures = []
temp_var = ""
print("This program takes in a list of temperatures and prints the "
      "minimum, maximum, average temperature, "
      "and total number of temperatures.")
print("If you wish to end the program and print the min, max, average, "
      "and total number of temperatures, enter 'Quit'")


def main(user_input):
    while (user_input != "Quit" or user_input != "No"):
        try:
            if user_input == "Yes":
                pass
            if user_input == "No":
                break
            user_input = input("Enter temperature and hit enter or type 'Quit' and hit enter to end the list: ")
            temperatures.append(int(user_input))
            if user_input == "Quit":
                break
        except ValueError:
            break
        try:
            if user_input == 0:
                temperatures.append(int(user_input))
                pass
            elif type(user_input is int) == True:
                pass
            elif type(user_input is float) == True:
                pass
            elif (type(user_input is float) == False) and (user_input == "Quit"):
                break
        except ValueError: print("Please enter a temperature or a number next time. Thank you.")
        try:
            if user_input == "Quit":
                break
            elif int(user_input) == True:
                pass
            elif float(user_input) == True:
                pass
            elif type(int(user_input) is str != 'No') == True:
                print("Please enter a temperature or a number next time. Thank you. ")
                pass
            elif type(int(user_input) is str != 'Quit') == True:
                print("Please enter a temperature or a number next time. Thank you. ")
                pass
            elif type(float(user_input) is str != 'No') == True:
                print("Please enter a temperature or a number next time. Thank you. ")
                pass
            elif type(float(user_input) is str != 'Quit') == True:
                print("Please enter a temperature or a number next time. Thank you. ")
                pass
            elif type(user_input is str == 'Quit') == True:
                break
        except ValueError: print("Please enter a temperature or a number next time. Thank you. ")
    return(temperatures)

user_input = input("Would you like to enter temperatures? Enter 'Yes' or 'No': ")


main(user_input)

# Parse data
try:
    if len(temperatures) > 0:
        # Find relevant data points
        min_temp = min(temperatures)
        max_temp = max(temperatures)
        len_temp = len(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        sorted_temp = sorted(temperatures)

        # Output data to user
        print("Your temperatures were: ", sorted_temp)
        print("Your minimum temperature is ", min_temp, end='\n')
        print("Your maximum temperature is ", max_temp, end='\n')
        print("Your average temperature is ", "%0.2f" % mean_temp, end='\n')
        print("Your total number of temperatures is ", len_temp, end='\n')
    pass
except ValueError: print("Cannot provide data with zero inputs")



