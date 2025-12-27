"""
******************************
CS 1026A Fall 2025
Assignment 4: Blackjack
Created by: Xiaojun Huang
Student ID: xhuan527
Student Number: 251480051
File created: December 9, 2025
******************************
This file is the Game class, which represents the actual Blackjack game and contains the various actions and processes to allow the game to be played out, importing the Deck and Hand classes as a foundation (one example is passing the total to the game, in a format of either integer or tuple).
For the game itself, it will always be one human player (the user) against one computer player.
The players can each take alternating turns to draw cards from the shuffled deck to reach a best total of 21, given that them are not busted yet.
After each round, the best total of both players will be evaluated, and the user can choose to continue with a new round or end the game.
Once the game is finished, the results of all rounds of that game are written to a text file, under the file name that the user entered.
"""

from Deck import *
from Hand import *
class Game:
    def __init__(self, num_decks = 1):
        self._deck = Deck(num_decks)
        self._deck.shuffle()
        self._player_hand = Hand()
        self._comp_hand = Hand()
        self._player_active = True
        self._comp_active = True
        self._results = []

    def play(self):
        self.play_round() # First round
        while True:
            continue_game = input("Do you want to play again? (yes/no): ")
            if continue_game == "yes":
                self.play_round()
            elif continue_game == "no":
                break
        while True: # If the player type in something that does not end with that extension, continue prompting them until they do type in a valid filename
            filename = input("Enter filename (ending in .txt) for the game results: ")
            if filename.endswith(".txt"):
                self.output_game_results(filename)
                break

    def get_player_best(self): # Using a helper function for simplicity.
        if type(self._player_hand.total()) == int:
            return self._player_hand.total() # Represents the case of the player not having any ace. The best total is simply the total
        else: # If the player does have one or more aces, the best total is the larger element in the tuple, or the smaller element if the larger element exceeds 21
            if max(self._player_hand.total()) > 21:
                return min(self._player_hand.total())
            else:
                return max(self._player_hand.total())

    def get_comp_best(self): # Applying the same logic for the computer
        if type(self._comp_hand.total()) == int:
            return self._comp_hand.total()
        else:
            if max(self._comp_hand.total()) > 21:
                return min(self._comp_hand.total())
            else:
                return max(self._comp_hand.total())

    def get_comp_least(self): # This helper function helps for the case of the computer determining if the total/smaller element of the tuple is smaller than 17
        if type(self._comp_hand.total()) == int:
            return self._comp_hand.total()
        else:
            return min(self._comp_hand.total())

    def play_round(self):
        self._player_hand = Hand() # Creating new empty hand for each round
        self._comp_hand = Hand()

        self._player_active = True # Setting both active for new round
        self._comp_active = True

        self._player_hand.add_card(self._deck.draw_card()) # Dealing cards in an alternating pattern
        self._comp_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())

        print(self._player_hand) # Print out the hands of both player and computer, this will return a string as the Hand object defines how to output a string representing the hand
        # print(self._comp_hand)

        # Initial checks
        if self.get_player_best() > 21:
            self._player_active = False # The player busted, so they cannot ask for new cards
        else:
            self._player_active = True

        if type(self._comp_hand.total()) == tuple and max(self._comp_hand.total()) == 21:
            print("Determine what computer will do (hit/stand)")
            print("stand")
            print(self._player_hand)
            # print(self._comp_hand)
            self._comp_active = False
        elif self.get_comp_best() > 21:
            self._comp_active = False # Even if the computer busted, the player does not know in a real game, and they can still choose to continue
        else:
            self._comp_active = True

        while self._player_active:
            move = input("What do you want to do? Type 'hit' for another card or 'stand' if you are done.\n")
            if move == "hit":
                self._player_hand.add_card(self._deck.draw_card())
                if self.get_player_best() > 21:
                    self._player_active = False # The player busted, so they cannot ask for new cards
                    print(self._player_hand)
                    # print(self._comp_hand)
                # I was including a case of the total being equal to 21 and then exiting the while loop, but it should not be included as the loop only stops if the player is busted or they choose to stand
                else:
                    #### DETERMINING WHAT THE COMPUTER WILL DO AFTER THE PLAYER HITS
                    if type(self._comp_hand.total()) == tuple and max(self._comp_hand.total()) == 21: # If the Computer has one or more aces and have exactly 21 as their higher value, they will stand. This is put before the "<17" rule as it is an exception to the rule, so if this is satisfied, then the "elif" clause for the rule will be skipped
                        print("Determine what computer will do (hit/stand)")
                        print("stand")
                        print(self._player_hand)
                        # print(self._comp_hand)
                        self._comp_active = False # Should not exit the loop here as the player still has a chance to get 21
                    elif self.get_comp_least() < 17:
                        print("Determine what computer will do (hit/stand)")
                        print("hit")
                        self._comp_hand.add_card(self._deck.draw_card())
                        print(self._player_hand)
                        # print(self._comp_hand)
                        if self.get_comp_best() > 21:
                            self._comp_active = False  # Even if the computer busted, the player does not know in a real game, and they can still choose to continue
                    else:
                        print("Determine what computer will do (hit/stand)")
                        print("stand")
                        print(self._player_hand)
                        # print(self._comp_hand)
                        self._comp_active = False
            elif move == "stand":
                print(self._player_hand)
                # print(self._comp_hand)
                self._player_active = False

        # If the player chooses to stand and the computer is still active:
        while self._comp_active:
            if self.get_comp_least() < 17: # Potential hits, check for the exception
                if type(self._comp_hand.total()) == tuple and max(self._comp_hand.total()) == 21: # This exception can indeed occur, if the total is a tuple and the smaller element is less than 17
                    print("Determine what computer will do (hit/stand)")
                    print("stand")
                    print(self._player_hand)
                    # print(self._comp_hand)
                    self._comp_active = False
                else:
                    print("Determine what computer will do (hit/stand)")
                    print("hit")
                    self._comp_hand.add_card(self._deck.draw_card())
                    print(self._player_hand)
                    # print(self._comp_hand)
                    if self.get_comp_best() > 21:
                        self._comp_active = False
                    # elif self.get_comp_best() == 21:
                    #     self._comp_active = False
            else: # No matter what, the computer will stand if the best total is larger than 17
                print("Determine what computer will do (hit/stand)")
                print("stand")
                print(self._player_hand)
                # print(self._comp_hand)
                self._comp_active = False

        if not self._player_active and not self._comp_active: # The round ends when neither the player nor the computer is active
            # We separate each case to the point where a distinct list can be appended to the results, e.g. although the computer wins the first two cases, for one the player is busted and for the other they are not
            if self.get_player_best() > 21 and self.get_comp_best() <= 21: # The player is busted, the computer is not
                print("The round has ended. Winner: Computer")
                self._results.append(["Player: bust", f"Computer: {self.get_comp_best()}", "Winner: Computer"])
            elif self.get_comp_best() > self.get_player_best() and self.get_comp_best() <= 21: # Both did not bust, but the computer has a higher best total
                print("The round has ended. Winner: Computer")
                self._results.append([f"Player: {self.get_player_best()}", f"Computer: {self.get_comp_best()}", "Winner: Computer"])
            elif self.get_comp_best() > 21 and self.get_player_best() <= 21: # The computer is busted, the player is not
                print("The round has ended. Winner: Player")
                self._results.append([f"Player: {self.get_player_best()}", "Computer: bust", "Winner: Player"])
            elif self.get_player_best() > self.get_comp_best() and self.get_player_best() <= 21: # Both did not bust, but the player has a higher best total
                print("The round has ended. Winner: Player")
                self._results.append([f"Player: {self.get_player_best()}", f"Computer: {self.get_comp_best()}", "Winner: Player"])
            elif self.get_comp_best() > 21 and self.get_player_best() > 21: # Both busted
                print("The round has ended. Winner: Neither")
                self._results.append(["Player: bust", "Computer: bust", "Winner: Neither"])
            elif self.get_comp_best() <= 21 and self.get_player_best() <= 21 and self.get_comp_best() == self.get_player_best(): # Neither busted, but same total
                print("The round has ended. Winner: Draw")
                self._results.append([f"Player: {self.get_player_best()}", f"Computer: {self.get_comp_best()}", "Winner: Draw"])
            return

    def output_game_results(self, filename):
        outfile = open(filename, "w")
        round_information = []
        round_counter = 0
        for round in self._results:
            round_counter += 1
            round.insert(0, f"Round {round_counter}") # Adding the round # for the first row
            round = "\n".join(round) # Each string (as an element) in the list is separated by a new line
            round_information.append(round)
        outfile.write("\n\n".join(round_information)) # Each string (for round information) is separated by an empty line
        outfile.close()

if __name__ == "__main__":
    game = Game()
    game.play()