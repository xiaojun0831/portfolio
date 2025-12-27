"""
******************************
CS 1026A Fall 2025
Assignment 3: Winter Olympics
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: November 4, 2025
******************************
This file is the user-input system that will allow users to enter commands to analyze data and have the option to write the results to files.
First, all the functions in the "olympics" file are imported. Then a loop will be executed to ask the user for the name of host file, followed by command strings formated in a specific way.
Different errors will be raised and the prompt is repeated, until the user types the case-insensitive word "quit".
Eventually, the command string will be parsed into either "country + country name in single quotation marks + file name" or "year + year as integer + file name", and those 3 parameters will be passed to the respective functions in "olympics".
"""

from olympics import *
def parse_command(text, host_dict):
    text_first_split = text.split(" ", 1)
    item_1 = text_first_split[0] # First, we separate the first word (command) from the text
    text_second_split = text_first_split[1].rsplit(" ", 1) # For the remaining portion (indexed at 1 after the first split), we split the filename starting from the right
    if item_1.lower() != "country" and item_1.lower() != "year": # Raising exception if the user types in a command other than "country" or "year"
        raise ValueError("Unknown command")
    item_2 = text_second_split[0].strip(" ") # After stripping it, index 0 after the split becomes the middle part of the text, and we want to make sure that it is either a number for year, or a country name that is surrounded by single quotation marks (we don't care about how many words are in between the quotation marks)
    if not item_2.isdigit(): # For the country case, our goal is to check if it is valid, and remove the quotation marks so that it can become a proper parameter that is getting passed to the functions in "olympics"
        if (not item_2[0] == "'") or (not item_2[-1] == "'"): # Raising exceptions for not being surrounded by single quotation marks (essentially meaning that the text cannot be split into the three parts as required)
            raise ValueError("Incorrect command parameters")
        item_2 = item_2.strip("'") # Remove the quotation marks
    item_3 = text_second_split[1] # The last part, which should be the file name for the output
    if not item_3.endswith(".txt"): # Raising exception if the user types in an output filename that does not end in ".txt"
        raise ValueError("Invalid filename")
    if item_1.lower() == "country":
        country = item_2 # We are not told to modify the country name input in any way other than removing the quotation marks, so 'CANADA' won't match to Canada's medal data
        output_country_results(item_3, host_dict, country) # The last component of the command string is used as filename; host_dict is passed to the function at first; and the country variable is defined as the second part (index 1)
    if item_1.lower() == "year":
        year = int(item_2) # Converting the year from string to integer
        output_year_results(item_3, host_dict, year)

def command_system():
    while True:
        host_data_filename = input("Enter host data filename: ")
        try:
            host_dict = load_hosts(host_data_filename)
            break
        except FileNotFoundError: # Raising exception if it cannot find the file with the given name
            print("Invalid host filename")
        except ValueError: # Raising exception if there is an issue in loading it due to incorrect formatting (i.e. the first column is not a year that can be cast to an int)
            print("Invalid host file format")
    while True: # The function will only terminate if quit is entered, that's where we just put "return" and exit
        command = input("Enter a valid command or type 'quit' to end the program: ")
        if command.lower() == "quit": # "quit" should be case-insensitive
            return
        try:
            parse_command(command, host_dict) # The host_dict is the actual host dictionary we loaded in the previous part, and that is taken as the parameter to be passed to the parse_command function
        except ValueError as e:
            print(str(e)) # Catching the exceptions from parse_command, printing out the custom message without crashing the program