# DSC 510
# Week 3
# Programming Assignment 3.1
# Author Makayla McKibben
# 06.17.2024
# Program Calculates Cost of Fiber Optic Cable Install and Print Receipt

# Change Control Log
#Change#:1
#Change(s) Made: Changed the greeting line 14
#Change#:2
#Change(s) Made: Added parameters for the user input ft. of cable lines: 20-26
#Date of Change: 06.14.2024
#Author: Makayla McKibben
#Change Approved by: Makayla McKibben
#Date Moved to Production: 06.14.2024

#Change#:3
#Change(s) Made: Editted cost to account for bulk pricing lines 67-75
#Change#:4
#Change(s) Made: Editted user input of number of feet to be a try/except
#lines 50-64
#Change#5:
#Change(s) Made: Editted cost of labor calculations lines 78-94
#Change#:6
#Change(s) Made: Ensuring integer or float values were used for calculations
#lines 97-101
#Date of Change: 06.17.2024
#Author: Makayla McKibben
#Change Approved by: Makayla McKibben
#Date Moved to Production: 06.17.2024

# Display User Welcome Message
print(
    "Welcome valued customer! "
    "This program will calculate the cost of installation of fiber optic cable.")

# Accept Company Name From User
company_name = input("Please enter your company name: ")

# Print parameters and instructions for user input for feet of cable
print("Please enter the number of feet of fiber optic cable needed.", end='\n')
print("Value must be between 1 and 1,000. ", end='\n')
print("If ordering more than 1,000ft call (555)123-4567 for quote.", end='\n')

# Accept Number of Feet of Fiber Optic Cable to be Installed
num_feet_cable = input("Please enter the number of feet now: ")

# Convert Number of Feet of Cable to Integer
try:
    num_feet_cable = int(num_feet_cable)
    if type(num_feet_cable) == int:
        pass
except:
    print("Please enter a number. "
          "If a number is not entered ,"
          "the program will not be able to perform this calculation.", end='n')
    num_feet_cable = input("Please enter the number of feet now: ")
    num_feet_cable = int(num_feet_cable)
    if type(num_feet_cable) == int or float:
        pass
    else:
        print("A number was not provided. The program will now close.")
        exit()

# Calculate Material Cost
if num_feet_cable <= 100:
    cost_of_materials = num_feet_cable * 0.87
elif num_feet_cable > 100 and num_feet_cable < 250:
    cost_of_materials = num_feet_cable * 0.80
elif num_feet_cable >= 250 and num_feet_cable < 500:
    cost_of_materials = num_feet_cable * 0.70
elif num_feet_cable >= 500:
    cost_of_materials = num_feet_cable * 0.50
    pass
# Calculate Cost of Installation
if num_feet_cable <= 100:
    cost_of_materials = num_feet_cable * 0.87
elif num_feet_cable > 100 and num_feet_cable < 250:
    cost_of_materials = num_feet_cable * 0.80
elif num_feet_cable >= 250 and num_feet_cable < 500:
    cost_of_materials = num_feet_cable * 0.70
elif num_feet_cable >= 500:
    cost_of_materials = num_feet_cable * 0.50
    pass

# Determine Cost of Labor
if num_feet_cable <= 100:
    cost_of_labor = 150
    pass
if num_feet_cable > 100 and num_feet_cable <= 250:
    cost_of_labor = 300
    pass
if num_feet_cable > 250 and num_feet_cable <= 500:
    cost_of_labor = 500
    pass
if num_feet_cable > 500 and num_feet_cable <= 1000:
    cost_of_labor = 800
    pass
if num_feet_cable > 1000:
    print(end='\n')
    print("Call (555) 123-4567 for specialty quote")
    exit()
    pass

# Calculate Total Cost
if cost_of_materials == int or float and cost_of_labor == int or float:
    total_cost = cost_of_materials + cost_of_labor
else:
    print("A value for the total cost cannot be provided. "
          "Call (555) 123-4567 for specialty quote")

# Format Costs to Two Decimal Places
cost_of_materials = format(cost_of_materials, ".2f")
cost_of_labor = format(cost_of_labor, ".2f")
total_cost = format(total_cost, ".2f")

# Print Receipt
print(end='\n')
print(company_name, "Receipt", end='\n')
print("Installation of", num_feet_cable, "feet of cable", end='\n')
print("Material Cost: $", cost_of_materials, end='\n')
print("Labor Cost: $", cost_of_labor, end='\n')
print("Total Cost: $", total_cost, end='\n')
print("Thank you for your business!", end='\n')