"""
******************************
CS 1026A Fall 2025
Assignment 3: Winter Olympics
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: November 4, 2025
******************************
This file contains all the functions to load data from files, write results into files, perform analysis of different kinds, and any other data-related operations for the program.
More specifically, if parameters are passed from "main" correctly, the functions can:
- Create and return a dictionary of hosts
- Load the medal data from a file of a specific year, if that file is found for that year
- Analyze the given country and write the results to a text file with the given filename
- Analyze the given year and write the results to a text file with the given filename
"""

def load_hosts(filename):
    infile = open(filename, "r")
    host_dict = {}
    for lines in infile:
        year = int(lines.split(",")[0].strip())
        # As the year is the before the first comma, we can split the lines, and the year will be at index 0 as a result
        # Additionally, we strip the year to clean it up, and we also convert that into an integer as required
        host_dict[year] = [lines.split(",")[1].strip(), lines.split(",")[2].strip(), lines.split(",")[3].strip()]
        # We repeat the same process for the remaining three columns in the csv file, and construct a list for the value part, as required
    infile.close() # We close the infile before returning "host_dict", as nothing in the function will be executed after the return statement
    return host_dict

def load_medals(filename):
    infile = open(filename, "r")
    dict_medals = {}
    infile.readline() # We do not want the header roll
    for lines in infile:
        country = lines.split(",")[0].strip()
        gold = int(lines.split(",")[1].strip())
        silver = int(lines.split(",")[2].strip())
        bronze = int(lines.split(",")[3].strip())
        dict_medals[country] = [gold, silver, bronze, gold + silver + bronze] # We have to manually add this because for the last column which is supposed to be the total medal count, some values are missing
    infile.close()
    return dict_medals

def try_load_medals(year):
    try: # As we cannot hardcode any year in, I use a try and except structure
        return load_medals("medals" + str(year) + ".csv") # We concatenate using the year, to form the "actual parameter" for the "filename" argument
    except FileNotFoundError:
        return None

def output_country_results(filename, host_dict, country):
    outfile = open(filename, "w")
    all_the_countries = []
    for item in host_dict.values():
        all_the_countries.append(item[1])
    # We want to get all the countries that is in the dictionary, so I wrote a for loop to extract all the "index 1s" in the values for the dictionary, and put them into a list
    outfile.write(str(country) + "\n\n") # We need a blank line after the country name, so we add 2 newline characters

    if country in all_the_countries:
        outfile.write("Olympics hosted in this country:\n")
        outfile.write(" ".join(["Year", "Type", "City"]) + "\n")
        for key, value in host_dict.items():
            if country in value:
                outfile.write(" ".join([str(key), value[2], value[0]]) + "\n") # Each corresponds to the year, type of the Olympics, and the city
        outfile.write("\n")
    else:
        outfile.write("No Olympics hosted in this country.\n\n")

    appearances = [] # We want to check if the country is in any medal data file that are available (not just the ones that are currently given)
    for year in range(2000, 10000): # We know that we are starting from 2000. To be safe, we will check all possible four-digit numbers that could be in the medal data file name, which means from 2000 to 9999.
        data = try_load_medals(year)
        if data is not None: # Narrowed down to the years that we have the data
            if country in data: # If the country is present in any of those years
                appearances.append(year)
    if len(appearances) == 0:
        outfile.write("No Olympic appearances by this country.")
    else:
        outfile.write("Olympic appearances by this country:\n")
        outfile.write(" ".join(["Year", "Gold", "Silver", "Bronze", "Total"]) + "\n")
        # As the lines for the medal counts are written into the file via a for loop, we cannot put a newline character after each line, as this will create a blank line at the end. Therefore, my thought is to have the lines first, and then join those lines by newline characters in between each line.
        lines_to_write = [] # We need a list for all the lines, or else, when we try to join the lines, the newline will be added in between every number, which is not what we want.
        for year in appearances:
            for key, value in try_load_medals(year).items():
                if key == country:
                    line = " ".join([str(year), str(value[0]), str(value[1]), str(value[2]), str(value[3])]) # Corresponding to year, gold, silver, and bronze, respectively
                    lines_to_write.append(line)
        outfile.write("\n".join(lines_to_write))
    outfile.close()
    return

def output_year_results(filename, host_dict, year):
    outfile = open(filename, "w")
    if year % 2 == 0 or year == 2021: # Only even years have the Olympics except 2021, and we are only considering the games since 2020
        outfile.write(f"Year: {year}\n")
        outfile.write(f"Host: {host_dict[year][0]}, {host_dict[year][1]}\n")
        outfile.write(f"Type: {host_dict[year][2]}\n\n")
        medals = try_load_medals(year) # If we do not the medal data file for the year, then the try load medal function for that year will return None
        if medals is None: # We have Olympics for that year, it's just we don't have the dataset for it
            outfile.write(f"No medals data file available for {year}")
        else:
            medals = load_medals("medals" + str(year) + ".csv") # Load the medal list for that year
            max_gold = max([value[0] for value in medals.values()]) # Index 0 for the values in the dictionary created by load.medals corresponds to the number of gold medals
            outfile.write(f"Most gold medals: {max_gold} by ")
            most_gold_country = []
            for key, value in medals.items():
                if value[0] == max_gold:
                    most_gold_country.append(key)
            if len(most_gold_country) == 1:
                outfile.write(most_gold_country[0]) # If there is only one country in the list (no tie for first place), just write that country
            else:
                outfile.write(" and ".join(most_gold_country)) # If there is more than one element in the list (tie), write all the elements, joined by "and“
            outfile.write("\n")

            # Same thing for most silver, bronze, and total
            max_silver = max([value[1] for value in medals.values()])
            outfile.write(f"Most silver medals: {max_silver} by ")
            most_silver_country = []
            for key, value in medals.items():
                if value[1] == max_silver:
                    most_silver_country.append(key)
            if len(most_silver_country) == 1:
                outfile.write(most_silver_country[0])
            else:
                outfile.write(" and ".join(most_silver_country))
            outfile.write("\n")

            max_bronze = max([value[2] for value in medals.values()])
            outfile.write(f"Most bronze medals: {max_bronze} by ")
            most_bronze_country = []
            for key, value in medals.items():
                if value[2] == max_bronze:
                    most_bronze_country.append(key)
            if len(most_bronze_country) == 1:
                outfile.write(most_bronze_country[0])
            else:
                outfile.write(" and ".join(most_bronze_country))
            outfile.write("\n")

            max_total = max([value[3] for value in medals.values()])
            outfile.write(f"Most total medals: {max_total} by ")
            most_total_country = []
            for key, value in medals.items():
                if value[3] == max_total:
                    most_total_country.append(key)
            if len(most_total_country) == 1:
                outfile.write(most_total_country[0])
            else:
                outfile.write(" and ".join(most_total_country))
    else:
        outfile.write(f"No Olympics were held in {year}")
    outfile.close()
    return