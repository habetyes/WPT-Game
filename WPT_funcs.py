import random
import operator
import collections
import time

# Initialize Deck
def card_deck():
       return {1: 'Ah', 2: 'Kh', 3: 'Qh', 4: 'Jh', 5: 'Th', 6: '9h', 7: '8h', 8: '7h',
              9: '6h', 10: '5h', 11: '4h', 12: '3h', 13: '2h', 14: 'Ad', 15: 'Kd', 16: 'Qd', 17: 'Jd', 18: 'Td',
              19: '9d', 20: '8d', 21: '7d', 22: '6d', 23: '5d', 24: '4d', 25: '3d', 26: '2d', 27: 'Ac', 28: 'Kc', 29: 'Qc', 
              30: 'Jc', 31: 'Tc', 32: '9c', 33: '8c', 34: '7c', 35:'6c', 36:'5c', 37:'4c', 38:'3c', 39:'2c', 40:'As', 41:'Ks',
              42: 'Qs', 43:'Js', 44:'Ts', 45:'9s', 46:'8s', 47:'7s', 48:'6s', 49:'5s', 50:'4s', 51:'3s',52:'2s'}

# Hole Bonus check for pocket pairs
pair_bonus = {'A': 20, 'K': 8, 'Q': 8, 'J':8, 'T':3, '9':3, '8':3, '7':3, '6':3, '5':2,'4':2,'3':2,'2':2}

# Look up for String Representation of Value
value_dict = {1:'A', 2:'K', 3:'Q', 4:'J', 5:'T', 6:'9', 7:'8', 8:'7', 9:'6', 10:'5', 11:'4', 12:'3', 13:'2', 14:'A'}

# Key Value Pairs to determine which card is more "valuable" than another
cards_to_rank = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}

# Key Value Pairs for Straight Checks
straight_to_ranks = {'A': {1, 14}, 'K': {2}, 'Q': {3}, 'J': {4}, 'T': {5}, '9': {6}, '8': {7}, '7': {8}, '6': {9}, '5': {10}, '4': {11}, '3': {12}, '2': {13}}

# Straight Flush Dicts
res = {1: 'Ah', 2: 'Kh', 3: 'Qh', 4: 'Jh', 5: 'Th', 6: '9h', 7: '8h', 8: '7h',
       9: '6h', 10: '5h', 11: '4h', 12: '3h', 13: '2h', 14: 'Ah', 16: 'Ad', 17: 'Kd', 18: 'Qd', 19: 'Jd',
       20: 'Td', 21: '9d', 22: '8d', 23: '7d', 24: '6d', 25: '5d', 26: '4d', 27: '3d', 28: '2d', 29: 'Ad', 31: 'Ac', 32: 'Kc', 
       33: 'Qc', 34: 'Jc', 35: 'Tc', 36: '9c', 37: '8c', 38:'7c', 39:'6c', 40:'5c', 41:'4c', 42: '3c', 43:'2c', 44:'Ac',
       46: 'As', 47:'Ks', 48:'Qs', 49:'Js', 50:'Ts', 51:'9s', 52:'8s', 53:'7s', 54:'6s', 55:'5s',56:'4s', 57:'3s', 58:'2s', 59:'As'}

sf_dict = {'Ah': {1,14}, 'Kh': {2}, 'Qh': {3}, 'Jh': {4}, 'Th': {5}, '9h': {6}, '8h': {7}, '7h': {8}, '6h': {9}, '5h': {10},
           '4h': {11}, '3h': {12}, '2h': {13}, 'Ad': {16, 29}, 'Kd': {17}, 'Qd': {18}, 'Jd': {19}, 'Td': {20}, '9d': {21},
           '8d': {22}, '7d': {23}, '6d': {24}, '5d': {25}, '4d': {26}, '3d': {27}, '2d': {28}, 'Ac': {31, 44}, 'Kc': {32},
           'Qc': {33}, 'Jc': {34}, 'Tc': {35}, '9c': {36}, '8c': {37}, '7c': {38}, '6c': {39}, '5c': {40}, '4c': {41}, '3c': {42},
           '2c': {43}, 'As': {46, 59}, 'Ks': {47}, 'Qs': {48}, 'Js': {49}, 'Ts': {50}, '9s': {51}, '8s': {52}, '7s': {53}, '6s': {54},
           '5s': {55}, '4s': {56}, '3s': {57}, '2s': {58}}


# Function to intake and validate user inputs
def budget_validation(prompt, bankroll):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print ("Sorry, please enter a number")
            continue

        if value > bankroll:
            print ("Sorry, you don\'t have enough to make that bet")
            continue
        else:
            break
    return value

def raise_validation(prompt, ante, bankroll):
    while True:
        if (ante * 3) > bankroll:
            time.sleep(1)
            print("Sorry, you don\'t have enough chips to raise")
            time.sleep(2)
            all_in = "n"
            break
        else:
            all_in = input(prompt)
            break

    return all_in


# Function to deal hand for any number of players
def deal_player(deck):
    player_hand = []
    for x in range(2):
        player_hand.append(deck.pop(random.choice(list(deck.keys()))))    
    return player_hand

# Deals just the flop
def deal_game(deck):
       board = []
       for x in range(3):
              board.append(deck.pop(random.choice(list(deck.keys()))))
       print(board) 
       time.sleep(2)
       turn = deck.pop(random.choice(list(deck.keys())))
       board.append(turn)
       print(board)
       time.sleep(2)
       river = deck.pop(random.choice(list(deck.keys())))
       board.append(river)
       print(board)
       return board

def hole_bonus(hand):
       """Evaluates and returns hole card bonus payout"""
       suited = hand[0][1] == hand[1][1]

       if ((hand[0] == 'Ad') or (hand[0] == 'Ah')) and ((hand[1] == 'Ah') or (hand[1] == 'Ad')):
              hole_bonus_payout = 50
              print(f' RED ACES!!! Pays {hole_bonus_payout}:1')
       elif ((hand[0][0] == 'A') and (hand[1][0] == 'K')) or ((hand[0][0] == 'K') and (hand[1][0] == 'A')):
              if suited == True:
                     hole_bonus_payout = 25
                     print(f' Big Slick!! Pays {hole_bonus_payout}:1')
              else:
                     hole_bonus_payout = 0
                     print("Sorry, Bonus Bet Lost")
       elif hand[0][0] == hand[1][0]:
              pair = hand[0][0]
              hole_bonus_payout = pair_bonus[hand[0][0]]
              print(f'Pocket {pair}s! Pays {hole_bonus_payout}:1')
       elif suited == True:
              hole_bonus_payout = 1
              print(f'Suited! Pays {hole_bonus_payout}:1')
       else:
              hole_bonus_payout = 0
              print("Sorry, Bonus Bet Lost")
       return hole_bonus_payout

def showdown_hand(player, board):
       """Identifies final 7 card hand for each player/dealer"""
       final_hand = player + board
       return final_hand

def is_straight_flush(final_hand):
       """Identifies whether a player has a straight flush"""    
       sf_keys = set()
       sf_value_keys = set()
       for card in final_hand:
              sf_keys |= sf_dict[card]
              sf_value_keys |= straight_to_ranks[card[0]]
       sf_value_keys = sorted(sf_value_keys)
       sf_keys = sorted(sf_keys)

       for idx, value in enumerate(sf_keys):
              slice = sf_keys[idx:idx+5]
              if len(slice) < 5:
                     straight_flush = False
                     break
              if slice == list(range(value, value+5)):
                     straight_flush = True
                     sf_showdown = [res[value] for value in slice]
                     sf_values = [cards_to_rank[x[0]] for x in sf_showdown]
                     break
              else:
                     straight_flush = False                    

       return straight_flush

def straight_flush_values(final_hand):
       """Identifies the card rank values in the straight flush"""
       sf_keys = set()
       sf_value_keys = set()
       for card in final_hand:
              sf_keys |= sf_dict[card]
              sf_value_keys |= straight_to_ranks[card[0]]
       sf_value_keys = sorted(sf_value_keys)
       sf_keys = sorted(sf_keys)
       values = []
       for idx, value in enumerate(sf_keys):
              slice = sf_keys[idx:idx+5]
              if len(slice) < 5:
                     straight_flush = False
                     break
              if slice == list(range(value,value+5)):
                     straight_flush = True
                     sf_showdown = [res[value] for value in slice]
                     break
              else:
                     straight_flush = False


       if straight_flush == True:
              for idx, value in enumerate(sf_value_keys):
                     slice = sf_value_keys[idx:idx+5]
                     if slice == list(range(value,value+5)):
                            values = [value for value in slice]
                            break
       return values

def is_royal(final_hand):
    """
    Takes in straight flush keys and checks against Royal Flush
    """
    royal_flush = False
    straight_flush = is_straight_flush(final_hand)
    if straight_flush == True:
        sf_showdown = straight_flush_values(final_hand)
        if sf_showdown[0] == 1:
            royal_flush = True
        else:
            royal_flush = False
    return royal_flush

def is_flush(hand):
    c = collections.Counter(x[1] for x in hand)
    top_suit = c.most_common(1)[0][1]
    if top_suit > 4:
        flush = True
    else:
        flush = False
    return flush

def flush_check(hand):
    """
    First class function flush_check takes a final hand and uses Counter to check for flushes
    """
    c = collections.Counter(x[1] for x in hand)
    suit_count = c.most_common(1)[0][1]
    top_suit = c.most_common(1)[0][0]
    if suit_count > 4:
        flush = True
    else:
        flush = False
    
    def flush_keys():
        """
        Closure will append keys from the flush cards when flush is true 
        """
        keys = []
        if flush == True:
            for x in hand:
                if x[1] == top_suit:
                    keys.append(cards_to_rank[x[0]])
        keys = sorted(keys)
        # Return Keys that can be used later 
        return keys
    
    return flush_keys

def is_straight(hand):
    keys = set()
    for card in hand:
        keys |= straight_to_ranks[card[0]]
    keys = sorted(keys)

    for idx, value in enumerate(keys):
        slice = keys[idx:idx+5]
        if len(slice) < 5:
            straight = False
            break
        if slice == list(range(value,value+5)):
            straight = True
            straight_top_key = value
            straight_top = value_dict[value]
            break
        else:
            straight = False
            
    return straight

def straight_check(hand):
    """First class function takes final hand and checks for straight"""
    keys = set()
    for card in hand:
        keys |= straight_to_ranks[card[0]]
    keys = sorted(keys)

    for idx, value in enumerate(keys):
        slice = keys[idx:idx+5]
        if len(slice) < 5:
            straight = False
            break
        if slice == list(range(value,value+5)):
            straight = True
            straight_top_key = value
            straight_top = value_dict[value]
            break
        else:
            straight = False
            
    def straight_keys():
        """Closure will identify the 5 card straight hand and return the keys"""
        if straight == True:
            return slice
            
    return straight_keys

def common_cards(hand):
    """Check for common cards to be used in quads, full house, trips and pairs"""
    card_sort = sorted(cards_to_rank[x[0]] for x in hand)
    c = collections.Counter([x for x in card_sort])   
    common = c.most_common(7)
    return common

def is_quads(final_hand):
    """Receives the result from common_cards function to check for quads"""
    common_card_list = common_cards(final_hand)
    if common_card_list[0][1] > 3:
        quads = True
    else:
        quads = False
    return quads

def is_full_house(final_hand):
    """Receives the result from common_cards function to check for Full House"""
    common_card_list = common_cards(final_hand)    
    if common_card_list[0][1] == 3 and common_card_list[1][1] >= 2:
        full_house = True
    else:
        full_house = False
    return full_house

def is_trips(final_hand):
    """Receives the result from common_cards function to check for Trips"""
    common_card_list = common_cards(final_hand)  
    if common_card_list[0][1] == 3 and common_card_list[1][1] < 2:
        trips = True
    else:
        trips = False
    return trips

def is_two_pair(final_hand):
    """Receives the result from common_cards function to check for Trips"""
    common_card_list = common_cards(final_hand)    
    if common_card_list[0][1] == 2 and common_card_list[1][1] == 2:
        two_pair = True
    else:
        two_pair = False
    return two_pair

def is_pair(final_hand):
    """Receives the result from common_cards function to check for Trips"""
    common_card_list = common_cards(final_hand)  
    if common_card_list[0][1] == 2 and common_card_list[1][1] < 2:
        pair = True
    else:
        pair = False
    return pair

def is_high_card(final_hand):
    common_card_list = common_cards(final_hand)  
    if common_card_list[0][1] == 1 and common_card_list[1][1] == 1:
        high_card = True
    else:
        high_card = False
    return high_card

def best_hand(hand):
    """Hand: A players final hand (hole cards plus board). Returns a dictionary with all aspects needed to evaluate hand winner"""
    if is_royal(hand):
        hand_name = "Royal Flush"
        showdown_strength = 1
        final_hand_bonus = 500
        final_hand_keys = straight_flush_values(hand)
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_straight_flush(hand):
        hand_name = "Straight Flush"
        showdown_strength = 2
        final_hand_bonus = 100
        final_hand_keys = straight_flush_values(hand)
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_quads(hand):
        hand_name = "Quads"
        showdown_strength = 3
        final_hand_bonus = 40
        final_hand_keys =[common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[1][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_full_house(hand):
        hand_name= "Full House"
        showdown_strength = 4
        final_hand_bonus = 8
        final_hand_keys = [common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[1][0], common_cards(hand)[1][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_flush(hand):
        hand_name = "Flush"
        showdown_strength = 5
        final_hand_bonus = 6
        flushes = flush_check(hand)
        final_hand_keys = flushes()
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_straight(hand):
        hand_name = "Straight"
        showdown_strength = 6
        final_hand_bonus = 4
        straights = straight_check(hand)
        final_hand_keys = straights()
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_trips(hand):
        hand_name = "Trips"
        showdown_strength = 7
        final_hand_bonus = 2
        final_hand_keys = [common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[1][0], common_cards(hand)[2][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_two_pair(hand):
        hand_name = "Two Pair"
        showdown_strength = 8
        final_hand_bonus = 0
        final_hand_keys =[common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[1][0], common_cards(hand)[1][0], common_cards(hand)[2][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    elif is_pair(hand):
        hand_name = "Pair"
        showdown_strength = 9
        final_hand_bonus = 0
        final_hand_keys =[common_cards(hand)[0][0], common_cards(hand)[0][0], common_cards(hand)[1][0], common_cards(hand)[2][0], common_cards(hand)[3][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}
    else:
        hand_name = "High Card"
        showdown_strength = 10
        final_hand_bonus = 0
        final_hand_keys =[common_cards(hand)[0][0], common_cards(hand)[1][0], common_cards(hand)[2][0], common_cards(hand)[3][0], common_cards(hand)[4][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown}

def winning_player(player_hand, dealer_hand):
    """Takes two hands and identifies winner"""
    player = best_hand(player_hand)
    dealer = best_hand(dealer_hand)
    
    if player["strength"] < dealer["strength"]:
        winner = "player"
    elif player["strength"] > dealer["strength"]:
        winner = "dealer"
    elif player["strength"] == dealer["strength"]:
        if player["top"] < dealer["top"]:
            winner = "player"
        elif player["top"] > dealer["top"]:
            winner = "dealer"
        elif player["top"] == dealer["top"]:
            if player["kicker"] < dealer["kicker"]:
                winner = "player"
            elif player["kicker"] > dealer["kicker"]:
                winner = "dealer"
            elif player["kicker"] == dealer["kicker"]:
                if player["kicker2"] < dealer["kicker2"]:
                    winner = "player"
                elif player["kicker2"] > dealer["kicker2"]:
                    winner = "dealer"
                elif player["kicker2"] == dealer["kicker2"]:
                    if player["kicker3"] < dealer["kicker3"]:
                        winner = "player"
                    elif player["kicker3"] > dealer["kicker3"]:
                        winner = "dealer"
                    elif player["kicker3"] == dealer["kicker3"]:
                        if player["kicker4"] < dealer["kicker4"]:
                            winner = "player"
                        elif player["kicker4"] > dealer["kicker4"]:
                            winner = "dealer"
                        elif player["kicker4"] == dealer["kicker4"]:
                            winner = "push"
    return winner