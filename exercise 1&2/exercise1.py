# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:55:38 2021

Assignment 1: Blackjack
T


@author: Daniel Broderick
"""

import random
import sys
import time

class deck:
    def __init__(self):
        suit = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K','A']
        self.deck = suit[:] +suit[:] + suit[:] + suit[:]
    
    def draw(self):
        drawn_card = self.deck.pop(random.randint(0, len(self.deck)-1))
        return drawn_card
        
    
def options(s):
    """
    Gives the user control over when to exit
    """
    if s.lower() == 'y' or s.lower() == 'yes':
        deck1 = deck() # create the deck
        round(deck1) # play a round
        
    elif s.lower() == 'n' or s.lower() =='no':
        print('goodbye')
        sys.exit()
    else:
        s = input('Sorry but I do not understand. Do you want to' + 
                  'play blackjack? Type "yes" or "no". \n\n')
        options(s)
        

def round(p_deck):
    """
    Take the provided deck and deal two cards to the player and dealer
    """
    player_hand = [p_deck.draw()]
    dealer_hand = [p_deck.draw()]
    player_hand.append(p_deck.draw()) 
    dealer_hand.append(p_deck.draw())
    
    player_turn(p_deck, player_hand, dealer_hand)

        
def player_turn(p_deck, player_hand, dealer_hand):
    """Tells the player what is in their hand, and the dealer's hand
    """

    s = input(f"Your hand: {player_hand}. The dealer's hand contains " +
              f"a facedown card and a '{dealer_hand[1]}'. Would " +
              "you like to hit or stay? (h/s) \n \n")

    if s.lower() == 'hit' or s.lower() == 'h':
        p_hit(p_deck, player_hand, dealer_hand)
        

    elif s.lower() == 'stay' or s.lower() == 's':
        print(f"Okay! The Dealer reveals his entire hand: {dealer_hand} \n\n")
        dealer_turn(p_deck, player_hand, dealer_hand)
    
    else:
        s = input("I don't understand. Let's try this again okay? \n \n")
        time.sleep(3)
        player_turn(p_deck, player_hand, dealer_hand)
        return



def dealer_turn(p_deck, player_hand, dealer_hand):
    time.sleep(2)

    while True:
    # The dealer stays with hands greater than or equal to 17 points
        if calculate(dealer_hand) >= 17:
            if calculate(dealer_hand) > 21:
                print("The dealer busts! You win with a hand of: {player_hand}")
                another_round(p_deck)
                return
            if calculate(player_hand)== calculate(dealer_hand):
                print("It's a draw!")
                another_round(p_deck)
                return
            if calculate(player_hand) < calculate(dealer_hand):
                print("You lose!")
                another_round(p_deck)
                return
            if calculate(player_hand) > calculate(dealer_hand):
                print("You win!")
                another_round(p_deck)
                return
                
                
        else: # the dealer hits
            print("the dealer hits")
            dealer_hand.append(p_deck.draw())
            time.sleep(2)
            print(f"the dealer's new hand is: {dealer_hand}")


def p_hit(p_deck, player_hand, dealer_hand):
    """draws a card for the player 
    """ 
    player_hand.append(p_deck.draw())
   
    if calculate(player_hand) > 21: #detects a bust
            print(f"You bust! The dealer wins with {dealer_hand}")
            time.sleep(2)
            another_round(p_deck)

    # call the function again, player can hit again
    player_turn(p_deck, player_hand, dealer_hand)
    


def another_round(deck):
    time.sleep(2)
    s=input("Want to play another round? (y/n)) \n")
    
    if s.lower()=='y' or s.lower()=='yes':
        if len(deck) < 20: # no universal rule for when to reshuffle
            time.sleep(2)
            print("reshuffling.....")
            deck = deck() # reshuffle, i.e. make anew deck
        
        #play another round
        round(deck)
    else:
        print("goodbye")
        

def main():
    """ driver function
    """
    s = input('Hello. I am your dealer. Would you ' +
          'like to play blackjack? (y/n) \n\n')
    options(s)    
    


def calculate(hand):
    """calculates the value of a hand, this function is ridiculous
    """
    # use a dictionary to store the value of each card
    values = {'2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              '10': 10,
              'J': 10,
              'Q': 10,
              'K': 10,
        }
    total = 0
    A_count = 0
    for x in hand:
        if x == 'A':
            A_count+=1
        else:
            total += values[x]
    
    
    if A_count == 0:
        return total
    
    # now we handle the Aces 
    if A_count == 1:
        if total <= 10:
            return 11+total
        elif total > 10:
            return 1 +total 
        
    # in case there are multiple Aces 
    if A_count == 2:
        if total <10:
            return 12 + total
        if total >=10:
            return 2+total
    if A_count == 3:
        if total <9:
            return 13 +total 
        if total >= 9:
            return 3 +total
    if A_count == 4:
        if total <8:
            return 14+ total
        if total >=8:
            return 4+total
    if A_count == 5:
        print("something went very wrong")
    

if __name__ == "__main__":
    main()
