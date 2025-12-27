"""
******************************
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: December 9, 2025
******************************
This file is the Hand class, which represents one player's hand in Blackjack.
The hand contains only one instance variable, which is a list to contain the cards (objects of the Card class) in the hand.
Additionally, the way of representing the total is defined; the string representing all cards in the hand and their total is also defined, which is useful for the Game class to print the hands of the players.
"""

from Card import *
class Hand:
    def __init__(self):
        self._hand = [] # Initializing the instance variable as an empty list

    def add_card(self, card):
        self._hand.append(card) # Adding the given card into the hand by appending to the list

    def total(self):
        ranks = []
        for card in self._hand:
            ranks.append(card.get_rank()) # Defined in the Card class previously
        if "A" not in ranks:
            total = 0 # Initializing total as an integer
            for rank in ranks: # Adding the number for each numerical rank, and 10 for each face card
                if rank in ("J", "Q", "K"):
                    total += 10
                else:
                    total += int(rank)
        else:
            total = [0, 0] # First creating a list for easier manipulation, then turning into a tuple
            ace_count = 0
            for rank in ranks:
                if rank == "A":
                    ace_count += 1
                    total[0] += 1 # The approach we use is that treat all the aces as 1 first, then as we know at most one ace can take the value of 11 (or else the hand will be busted), the higher element of the tuple will just be 10 more than the lower element. If there is only one ace, we just add 11 to make the higher element.
                elif rank in ("J", "Q", "K"):
                    total[0] += 10
                    total[1] += 10
                else:
                    total[0] += int(rank)
                    total[1] += int(rank)
            if ace_count > 1:
                total[1] = total[0] + 10
            else:
                total[1] += 11
            total = tuple(total)
        return total

    def __str__(self):
        if len(self._hand) > 0:
            total = self.total() # Getting the total by calling the total(self) method
            return "{" + f"{", ".join(str(card) for card in self._hand)}" + "}" + f", Total: {total}" # As there are curly brackets in the string, we separate them with the curly brackets for the f string to avoid confusion
        else:
            return "Empty hand"
