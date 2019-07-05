import random
import operator
import collections
import time
from WPT_funcs import *

# Initialize bankroll amount

bankroll = int(input("How much would you like to buy in for?"))

play = input(f'Welcome to WPT! Here\'s ${bankroll} to start. Would you like to play a hand?')

while play == "y":

    deck = card_deck()

    # Player input bet amounts and validate each bet amount against bankroll
    print(f'Starting Bankroll: {bankroll}')

    ante = budget_validation("How much would you like to ante: ", bankroll)
    bankroll -= ante
    hole_bonus_bet = budget_validation("How much would you like to bet on the Hole Card Bonus: ", bankroll)
    bankroll -= hole_bonus_bet
    final_bonus_bet = budget_validation("How much would you like to bet on the Final Hand Bonus: ", bankroll)
    bankroll -= final_bonus_bet

    time.sleep(1)

    # Deal hands for player and dealer
    player_hand = deal_player(deck)
    dealer_hand = deal_player(deck)

    # Show player hand and ask for a raise
    print(f'Player: {player_hand}')
    time.sleep(2)
  
    all_in = raise_validation("Would you like to raise? ", ante, bankroll)
    if all_in =="y":
        time.sleep(2)
        raised = ante * 3
        bankroll -= raised
    else:
        # Reassign ante and raise amounts so player gets paid nothing for folding while still being eligible for bonus payouts
        raised = 0 
        ante = 0

    # Show dealer hand after player raises
    print(f'Dealer: {dealer_hand}')
    time.sleep(2)

    # Evaluate hole card bonus result and adjusts bankroll accordingly
    if hole_bonus_bet > 0:
        hole_pay = hole_bonus(player_hand)
  
    if hole_pay > 0:
        bankroll += ((hole_bonus_bet * hole_pay) + hole_bonus_bet)
        time.sleep(2)
        print(f'Hole Bonus Wins ${hole_bonus_bet * hole_pay}')
        time.sleep(2)
        print(f'Post Hole Bonus Bankroll: ${bankroll}')
        

    # Initialize board and deal board cards
    time.sleep(2)
    board = deal_game(deck)

    # Identify final hands for player and dealer
    final_hand = showdown_hand(player_hand, board)
    dealer_final_hand = showdown_hand(dealer_hand, board)
    time.sleep(2)

    # Evaluate Final Hand Bonus
    if final_bonus_bet > 0:
        final_pay = best_hand(final_hand)["bonus"]

    if final_pay > 0:
        bankroll += ((final_bonus_bet * final_pay) + final_bonus_bet)
        print(f'{best_hand(final_hand)["hand"]}: Final Hand Bonus Wins ${final_bonus_bet * final_pay}') 
        time.sleep(2)
        print(f'Post Final Bonus Bankroll: ${bankroll}')
        time.sleep(2)
    
    # Evaluate winner and corresponing payout
    winner = winning_player(final_hand, dealer_final_hand)
    if winner == "player" and all_in == "y":
        payout = (ante * 2) + (raised * 2)
        winning_hand = best_hand(final_hand)["hand"]
        winning_showdown = best_hand(final_hand)["showdown"]
        print(f'{winner.capitalize()} wins with a {winning_hand} {winning_showdown}')
    elif winner == "player" and all_in != "y":
        payout = 0
        winning_hand = best_hand(final_hand)["hand"]
        winning_showdown = best_hand(final_hand)["showdown"]
        print(f'Scared money don\'t make money. You would have won with a {winning_hand}: {winning_showdown}')
    elif winner == "dealer" and all_in == "y":
        payout = 0
        winning_hand = best_hand(dealer_final_hand)["hand"]
        winning_showdown = best_hand(dealer_final_hand)["showdown"]
        print(f'{winner.capitalize()} wins with a {winning_hand} {winning_showdown}')
    elif winner == "dealer" and all_in != "y":
        payout = 0
        winning_hand = best_hand(dealer_final_hand)["hand"]
        winning_showdown = best_hand(dealer_final_hand)["showdown"]
        print(f'Good fold. Dealer would have won with a {winning_hand} {winning_showdown}')
    else:
        payout = ante + raised
        winning_hand = best_hand(final_hand)["hand"]
        winning_showdown = best_hand(final_hand)["showdown"]
        print(f'PUSH: {winning_hand} {winning_showdown}')

    bankroll += payout
    time.sleep(2)

    print(f'Post Hand Complete Bankroll: ${bankroll}')
    time.sleep(1)

    if bankroll <= 0:
        print("You are out of Money!")
        play = "n"
    else:
        play = input("Would you like to play another hand? ")