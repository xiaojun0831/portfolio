"""
******************************
CS 1026A Fall 2025
Assignment 2: Wordle
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: October 14, 2025
******************************
This file is a Wordle-like game, where the player will attempt to guess the correct word in 6 attempts.
First, the target word is chosen. This could either be chosen from an imported function where a random word is chosen in a list, or from a word that the developer assigns.
After that, the counter starts and the player enters their guess. The length will be checked first, and incorrect lengths will not be counted towards the number of attempts.
Then, the actual matching process will be executed as a two-pass, where the first pass checks for positions with exact matches, and then the second pass assigning the remaining positions to either partial matches or no matches.
The result is printed out as a string, where "!" represent exact matches, "*" represent partial matches, and "^" represent no matches.
If the target word is guessed, the program stops and prints out "You won!" If not, another guess is prompted until all 6 attempts are used up and the player loses.
"""

from randwords import *

def guess_word(length):
    guess = input() #Following after the "Guess #" prompt in the main function
    if len(guess) != length:
        print("Incorrect length.")
        return None
    return guess.upper()

def check_guess(guess, actual):
    """
    Originally, I did not plan to use a list, as I believe a for loop checking each letter in the range.
    However, this will result in "stealing" letters, and it caused a lot of trouble for me.
    For instance, if the actual word is "m__m_", and we input "m_mm_", it will show "!_*!_" instead of "!_^!_" due to the third position being checked first, violating the matching rule/
    Therefore, I eventually used lists to ensure that all the exact matches are checked before checking any partial marches.
    """
    result = [""] * len(guess) #Creating an empty list based on the length of the guessed word
    actual_in_list_form = list(actual) #Converting the actual word into a list

    #Recommended first pass: checking for exact matches
    for i in range(len(guess)):
        if guess[i] == actual[i]:
            result[i] = "!" #Putting the exclamation mark to the elements in the list for exact matches
            actual_in_list_form[i] = None #By changing the element in the actual word, we not only ensured that this letter will not get compared for partial matches again, but also kept the exclamation mark in the returned string

    #Second pass: checking for partial matches
    for i in range(len(guess)):
        if result[i] == "":
            if guess[i] in actual_in_list_form: #Right now we only need to check if the letter is in the actual characters list, as the exact matches are already removed previously
                result[i] = "*"
                actual_in_list_form[actual_in_list_form.index(guess[i])] = None #Using the same logic, by changing the element in the actual word to none as soon as a partial match is found, to avoid the same letter in the guess list being used again
            else:
                result[i] = "^" #If all of them are assigned, then we should return "^" for no match
    final_result = "" #Building the string combining all the elements in the list for return
    for char in result:
        final_result += char
    return final_result

def play_game(actual = ""):
    if actual == "":
        actual = get_rand_word().upper()  # Random for normal play
    else:
        actual = actual.upper() #Enable us to test specific cases, such as doubling letters, bypassing the random selection

    print(f"Word length: {len(actual)}")

    guess_counter = 1
    while guess_counter <= 6:
        print(f"Guess #{guess_counter}: ", end = "")
        guess = guess_word(len(actual))
        while guess is None: #When the length is incorrect, guess_word will return the sentinel value None, and then we re-prompt the player here, but that doesn't count towards the attempts
            print(f"Guess #{guess_counter}: ", end = "")
            guess = guess_word(len(actual)) #Run the guess_word function, and the guess.upper returned from the function is stored
        result = check_guess(guess, actual) #Run the check_guess function, and the string consisting symbols is returned as required
        print(result)

        if result == "!" * len(actual):
            print("You won!")
            return #Using return instead of break, as break will only exit the current loop, but return will exit the entire function

        guess_counter +=1

    print(f"You lost. The word was {actual}") #If "you won" is not reached after the 6 attempts, the player loses