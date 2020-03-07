import random
import operator
import collections
import time
from Poker import *
from itertools import cycle


# Functions to disposition the pot after a hand.
def adjustment(max_burn, pot):    
    adjust = min(pot, max_burn)
    return adjust

def bank_lost(bankroll, adjust):
    bankroll -= adjust
    return bankroll

def pot_lost(pot, adjust):
    pot += adjust
    return pot

def bank_won(bankroll, pot):
    bankroll += pot
    return bankroll

def pot_won(pot):
    pot = 0
    return pot


# Initialize game state
pot = 20
max_burn = 50

# Player bankroll initialization
player_bankroll = 495
NPC1_bankroll = 495
NPC2_bankroll = 495
NPC3_bankroll = 495

# Cycle through wild versions
versions = [None, low_wilds, bisexual]
version_cycle = cycle(versions)
next_version = next(version_cycle)
string_versions = ["Natural", "Semi-Natural", "Bisexual"]
string_cycle = cycle(string_versions)
next_string = next(string_cycle)

print("The game is Super-Beast. It will rotate between Natural, Semi-Natural, and Bisexual. Are you ready to play?")
time.sleep(2)
play = int(input("[1]: Play a hand \n[2]: Quit Game "))
while play == 1:
    # Iterate through wild types
    wild_type, next_version = next_version, next(version_cycle)
    wild_string, next_string = next_string, next(string_cycle)

    print(f'Currently Wild Type: {wild_string}')
    time.sleep(1)
    # Initialize deck and player hands and up card declaration
    deck = card_deck()
    player_hand = []
    dealer_hand = []
    up = True

    # Deal player first 4 cards and allow them to hold or fold
    deal_player(deck, player_hand, 4)
    print(player_hand)
    time.sleep(2)

    # Allow Player to buy extra cards for fours
    # Once NPCs are included randomly display whether they show that they bought a 4
    buy_fours(deck, player_hand)

    # ============ ENTER LOGIC FOR THE 3 - 2 - 1 - DROP!!! HERE=====================
    # Find out how to interrupt an input based on a length of time (enter any key to fold?)
    hold = int(input("[1]: Hold \n[2]: Drop "))

    if hold == 1:
        # Deal 3 cards +1 for every unbought four then deal an additional card for every additional four
        #========= Move cards owed into a function ===========
        cards_owed = 7 - len(player_hand) + keys(player_hand).count(11)
        while cards_owed != 0:
            deal_player(deck, player_hand, cards_owed, up)
            cards_owed = 7 - len(player_hand) + keys(player_hand).count(11)

        time.sleep(1.5)
        print(f'Player Hand: {best_hand(player_hand, wild_type)["hand"]}, {best_hand(player_hand, wild_type)["showdown"]}')
        time.sleep(1.5)
        print("\nThe Man's Hand")

        deal_player(deck, dealer_hand, 8, up)
        dealer_owed = 8 - len(dealer_hand) + keys(dealer_hand).count(11)
        while dealer_owed != 0:
            deal_player(deck, dealer_hand, dealer_owed, up)
            dealer_owed = 8 - len(dealer_hand) + keys(dealer_hand).count(11)

        time.sleep(1.5)
        print(f'The Man\'s Hand: {best_hand(dealer_hand, wild_type)["hand"]}, {best_hand(dealer_hand, wild_type)["showdown"]}')
        time.sleep(1)

        # Evaluate the winning hand if a player holds:
        # While hold == True:
        winner = winning_player(player_hand, dealer_hand, wild_type)
        if winner == "player":
            winning_hand = best_hand(player_hand, wild_type)["hand"]
            winning_showdown = best_hand(player_hand, wild_type)["showdown"]
            print(f'{winner.capitalize()} wins with a {winning_hand} {winning_showdown}')
        elif winner == "dealer":
            payout = 0
            winning_hand = best_hand(dealer_hand,wild_type)["hand"]
            winning_showdown = best_hand(dealer_hand, wild_type)["showdown"]
            print(f'The Man wins with a {winning_hand} {winning_showdown}')
        else:
            winning_hand = best_hand(player_hand, wild_type)["hand"]
            winning_showdown = best_hand(player_hand,wild_type)["showdown"]
            print(f'PUSH: {winning_hand} {winning_showdown}')


        

    # Once budgets are included change the below to if pot > 0: play = 1
    play = int(input("[1]: Play a hand \n[2]: Quit Game "))



"""
- Add multiple players (3 NPCs)
- Add logic that makes them hold if they have a "hand value" above a certain amount of points
- Could be an evaluate hand and anything better than trips they hold, 2+ wilds they hold, straight draw or flush draw they hold
    - May need to add 3 random cards to their hand in order to evaluate hand
- Could have multiple different levels (aggressive player, passive player, middle ground player)
- Add logic for pot and max burn
- use player_score function to evaluate who has the best hand and appropriately award them the pot while displaying their information
- May need to leverage dictionary to call-back winning players hand



"""