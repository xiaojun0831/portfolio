"""
******************************
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: November 29, 2025
******************************
This file is the Card class, which represents a single card from a standard deck of cards.
Each card has a rank (Ace, number 2-10, Jack, Queen, or King), and a suit (Spades, Hearts, Diamonds, or Clubs).
The file also defines the method of representing each card by a string, as well as comparing if two cards are equal. Both of them are useful in the Deck, Hand, and eventually Game classes.
"""

class Card:
    def __init__(self, rank, suit): # Setting up the initial state with two new attributes under the class and assigning value to them
        self._rank = rank
        self._suit = suit

    def get_rank(self): # Ensuring encapsulation by using a getter
        return self._rank

    def get_suit(self):
        return self._suit

    def __str__(self):
        return f"{self.get_rank().upper()}{self.get_suit().upper()[0]}" # Returning the string containing the card's rank and first letter of the card's suit in uppercase

    def __eq__(self, other):
        try:
            return self.get_rank() == other.get_rank() and self.get_suit() == other.get_suit() # The cards must have the same rank and suit in order to be considered equivalent
        except AttributeError: # If "other" is not a member of the Card class, then this will give an error, but we know that those cards are not equivalent as a result
            return False