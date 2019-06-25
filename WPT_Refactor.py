import random
import operator
import collections
import time
from WPT_funcs import *
# from WPT_funcs import board

# Initialize bankroll amount
bankroll = 300
play = "y"

while play == "y":

    deck = card_deck()

    # Player input an ante amount
    print(f'Starting Bankroll: {bankroll}')
    ante = int(input("How much would you like to ante? "))
    hole_bonus_bet = int(input("How much would you like to bet on the hole bonus "))
    final_bonus_bet = int(input("How much would you like to bet on the final hand bonus "))

    bankroll = bankroll - (ante + hole_bonus_bet + final_bonus_bet)

    # Deal hands for player and dealer
    player_hand = deal_player(deck)
    print(f'Post Player cards left {len(deck)}')
    dealer_hand = deal_player(deck)
    print(f'Post Dealer cards left {len(deck)}')

    # Show player hand and ask for a raise
    print(f'Player: {player_hand}')
    all_in = input("Would you like to raise? ")
    if all_in =="y":
        raised = ante * 3
        bankroll -= raised
    else:
        pass

    # Show dealer hand after player raises
    print(f'Dealer: {dealer_hand}')
    time.sleep(2)


    # Evaluate hole card bonus result and adjusts bankroll accordingly
    hole_pay = hole_bonus(player_hand)
    bankroll += (hole_bonus_bet * hole_pay)
    time.sleep(2)

    if hole_pay > 0:
        print(f'Hole Bonus Wins ${hole_bonus_bet * hole_pay}')
        time.sleep(2)

    print(f'Post Hole Bonus Bankroll: ${bankroll}')
    time.sleep(2)
    # Initialize board and deal board cards
    # board = []
    board = deal_game(deck)
    print(f'Post Board cards left {len(deck)}')

    # Identify final hands for player and dealer
    final_hand = showdown_hand(player_hand, board)
    dealer_final_hand = showdown_hand(dealer_hand, board)
    time.sleep(2)

    # Evaluate Final Hand Bonus
    final_pay = best_hand(final_hand)["bonus"]
    bankroll += (final_bonus_bet * final_pay)
    time.sleep(2)

    if final_pay > 0:
        print(f'Final Hand Bonus Wins ${final_bonus_bet * final_pay}') 
        time.sleep(2)   

    print(f'Post Final Bonus Bankroll: ${bankroll}')
    time.sleep(2)

    # Evaluate winner and corresponing payout
    winner = winning_player(final_hand, dealer_final_hand)
    if winner == "player":
        payout = (ante * 2) + (raised * 2)
        winning_hand = best_hand(final_hand)["hand"]
        winning_showdown = best_hand(final_hand)["showdown"]
        print(f'{winner} wins with a {winning_hand} {winning_showdown}')
    elif winner == "dealer":
        payout = 0
        winning_hand = best_hand(dealer_final_hand)["hand"]
        winning_showdown = best_hand(dealer_final_hand)["showdown"]
        print(f'{winner} wins with a {winning_hand} {winning_showdown}')
    else:
        payout = ante + raised
        winning_hand = best_hand(final_hand)["hand"]
        winning_showdown = best_hand(final_hand)["showdown"]
        print(f'PUSH: {winning_hand} {winning_showdown}')

    bankroll += payout
    time.sleep(2)

    print(f'Post Hand Complete Bankroll: ${bankroll}')

    play = input("Would you like to play another hand? ")