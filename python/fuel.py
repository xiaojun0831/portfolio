"""
******************************
CS 1026A Fall 2025
Assignment 1: Gas Station
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: September 19, 2025
******************************
This file is used to calculate the total cost to re-fuel based on the type of fuel and the number of litres of fuel needed.
This program will prompt the user for input and must verify that the inputs are valid.
Specific error messages will be printed out for invalid inputs.
The total cost after calculations for valid inputs will be printed out in a specific format with the dollar sign.
"""

type_of_fuel = (input("Select your fuel type: ").lower())
#Constant fuel prices
REGULAR_PRICE = 1.42
EXTRA_PRICE = 1.53
PREMIUM_PRICE = 1.60
DIESEL_PRICE = 1.75

if type_of_fuel == "regular" or type_of_fuel == "extra" or type_of_fuel == "premium" or type_of_fuel == "diesel": #Invalidate other fuel type inputs
    litres_of_fuel = input("How many litres of fuel do you need? ") #If the user did type in a valid fuel type, then the program prompts the user to enter the number of litres of fuel they need
    if "." in litres_of_fuel and "-" not in litres_of_fuel: #Invalidate entries without a decimal point, and the ones that are negative
        decimal = litres_of_fuel.find(".")
        if litres_of_fuel[decimal+1:].isdigit() and litres_of_fuel[:decimal].isdigit(): #Invalidate entries such as "25.", "$2.5" (anything with special characters except decimal), "ab.cd", and "2..5" (multiple decimals) by requiring the parts before and after the decimal must exist, and they both need to be only digits
            litres_of_fuel_converted = float(litres_of_fuel) #This step is only executed after previous checks, as if the user input is converted at the beginning, alpha/alphanumeric inputs will result in error
            if litres_of_fuel_converted == 0: #Invalidate entries such as "0.00" that managed to pass through the previous checks
                print("Invalid number of litres of fuel")
            else:
                #Calculate total price, based on different fuel types by using "if"s and "elif"s
                if type_of_fuel == "regular":
                    total_cost = REGULAR_PRICE * litres_of_fuel_converted
                elif type_of_fuel == "extra":
                    total_cost = EXTRA_PRICE * litres_of_fuel_converted
                elif type_of_fuel == "premium":
                    total_cost = PREMIUM_PRICE * litres_of_fuel_converted
                elif type_of_fuel == "diesel":
                    total_cost = DIESEL_PRICE * litres_of_fuel_converted
                print("Cost: $%.2f" % total_cost) #Final total cost printed out in the required format, keeping two decimal places
        else:
            print("Invalid number of litres of fuel")
    else:
        print("Invalid number of litres of fuel")
else:
    print("You selected an invalid fuel type")