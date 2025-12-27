"""
******************************
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: November 29, 2025
******************************
This file is the Deck class, which represents the deck of cards used in the Blackjack game.
There could be 52 cards in this deck or some multiple of 52 if multiple standard decks are being used for the game.
This class only has one instance variable which is a list containing all the Card objects (objects of the Card class).
Additionally, the method to shuffle the deck and to draw a card from the deck is defined, which will be useful for the Hand and Game classes.
"""

from Card import *
import random
class Deck:
    def __init__(self, num_decks):
        self._cards = []
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["clubs", "diamonds", "hearts", "spades"]
        for i in range(num_decks): # Iterate over the loop for multiple decks specified
            for suit in suits: # Creating all ranks in one suit first, as required
                for rank in ranks:
                    self._cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self._cards) # Shuffling the deck using the random library's method

    def draw_card(self):
        if len(self._cards) > 0:
            return self._cards.pop(0) # Removing and returning the very first (top) card in the deck (at index 0)
        else:
            return None # For the case where the deck is empty

