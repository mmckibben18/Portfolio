# DSC510
# Week 5
# Exercise 5.1
# Author: Makayla McKibben
# Date 07.05.2024

# Introduce program to user
print("This program can calculate addition, subtraction, multiplication"
      ", or division of two numbers.", end='\n')
print("It can also calculate an average of your values", end='\n')
print("You must enter ""Yes"" or ""No"" exactly as written")

# Ask user to initiate program
user_input = input("Would you like to run this program?: ")

# Defining main
def main(user_input):

    # Initiate While loop that runs the mathematical functions
    while user_input == "Yes":

        # Ask user if they want to use the first function which performs simple arithmetic
        user_requests_arithmetic = input("Would you like the program to perform"
                                         " simple arithmetic with two numbers? Yes or No: ")

        # If user wants to perform simple arithmetic this if statement takes the operater input
        if user_requests_arithmetic == "Yes":
            operator = input("Please enter your requested arithmetic operation."
                             " It can be +, -, *, or /: ")

            # Nested if that calls the function to use the specified operator
            if operator == "+":
                import performCalculation
                performCalculation.performCalculation(operator)
            elif operator == "-":
                import performCalculation
                performCalculation.performCalculation(operator)
            elif operator == "*":
                import performCalculation
                performCalculation.performCalculation(operator)
            elif operator == "/":
                import performCalculation
                performCalculation.performCalculation(operator)

            # Else that prints error if user supplied something other than an operator
            # Pass statement that ends nested if
            else:
                print("Invalid arithmetic operation. It can only be +, -, *, or /."
                      "This program will now pass to the next function.")
                pass

        # Else-if that skips the function if user does not want to perform simple arithmetic
        # Pass that ends the initial if statement
        elif user_requests_arithmetic == "No":
            print("Thank you! We'll move to the next program function.")
            pass

        # Statement that asks user if they'd like to run an average
        user_requests_average = input("Would you like the program to perform "
                                      "an average of a list of numbers? Yes or No: ")

        # If statement that calls the function which calculates the average
        if user_requests_average == "Yes":
            import calculateAverage
            calculateAverage.calculate_average()

        # Else-if that skips function if user does not want to calculate an average
        # Pass that ends the average function if statement
        elif user_requests_average == "No":
            print("Thank you! We'll move to the next program function.")
            pass

        # Asking user if they'd like to iterate through the loop again
        user_input = input("Would you like to use the program again? Type: "
                           "Yes or No: ")

        # If statement that notifies user they are starting the program over
        if user_input == "Yes":
            print("Thank you! We'll move to the beginning of the program.")

        # Else-if/pass that ends while loop
        elif user_input == "No":
            pass

# Call to main
main(user_input)