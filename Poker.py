import random
import operator
import collections
from collections import Counter
import time
from itertools import count, filterfalse 

# =============================================== DECK DICTIONARIES ========================================================
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
def deal_player(deck, player_hand, cards=2, up=False):
    for x in range(cards):
        player_hand.append(deck.pop(random.choice(list(deck.keys()))))
        if up == True:
            print(player_hand)
            time.sleep(2)
    return player_hand

# Deal variable amount of cards to board
def deal_game(deck, board, count=3):
    for x in range(count):
        board.append(deck.pop(random.choice(list(deck.keys()))))
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
                     time.sleep(1)
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
              time.sleep(1)
       return hole_bonus_payout

def showdown_hand(player, board):
       """Identifies final 7 card hand for each player/dealer"""
       final_hand = player + board
       return final_hand
    
# ====================================== WILD DEFINITIONS ============================================================
    
def low_wilds(hand):
    
    """Takes Final Hand, identifies wilds and static cards. Returns a dictionary with following keys
    wilds A count of the amount of wild cards
    static_keys: The Value Dict key value for the static cards
    static: The String Representation of all non-wild cards
    low: The Value Dict key value for the Wild Card
    wild_cards: The String representation of wild cards"""
    
    keys = [cards_to_rank[card[0]] for card in hand]
    low = max(keys)
    wilds = keys.count(low)
    
    for x in range(0,wilds):
        keys.remove(low)

    static = [card for card in hand if cards_to_rank[card[0]] in keys]
    wild_cards = [card for card in hand if cards_to_rank[card[0]] not in keys]
            
    return {"wilds": wilds, "static":static, "static_keys":keys, "low":low, "wild_cards": wild_cards, "wild_string": value_dict[low]}

def k_and_l(hand):
    
    """Takes Final Hand, identifies wilds and static cards. Returns a dictionary with following keys
    wilds A count of the amount of wild cards
    static_keys: The Value Dict key value for the static cards
    static: The String Representation of all non-wild cards
    low: The Value Dict key value for the Wild Card
    wild_cards: The String representation of wild cards"""
    
    keys = [cards_to_rank[card[0]] for card in hand]
    low = max(keys)
    kings = 2
    wilds = keys.count(low) + keys.count(kings)
    
    for x in range(0,keys.count(low)):
        keys.remove(low)
    for x in range(0, keys.count(kings)):
        keys.remove(kings)

    static = [card for card in hand if cards_to_rank[card[0]] in keys]
    wild_cards = [card for card in hand if cards_to_rank[card[0]] not in keys]
            
    return {"wilds": wilds, "static":static, "static_keys":keys, "low":low, "wild_cards": wild_cards, "wild_string": value_dict[low]}

def baseball(hand):
    """Takes Final Hand, identifies wilds and static cards. Returns a dictionary with following keys
    wilds A count of the amount of wild cards
    static_keys: The Value Dict key value for the static cards
    static: The String Representation of all non-wild cards
    low: The Value Dict key value for the Wild Card
    wild_cards: The String representation of wild cards"""
    
    keys = [cards_to_rank[card[0]] for card in hand]
    threes = 12
    nines = 6
    wilds = keys.count(threes) + keys.count(nines)
    
    for x in range(0,keys.count(threes)):
        keys.remove(threes)
    for x in range(0, keys.count(nines)):
        keys.remove(nines)

    static = [card for card in hand if cards_to_rank[card[0]] in keys]
    wild_cards = [card for card in hand if cards_to_rank[card[0]] not in keys]
            
    return {"wilds": wilds, "static":static, "static_keys":keys, "wild_cards": wild_cards}

def bisexual(hand):
    """ Identifies best hand between Baseball and Kings and Littles and returns that wild's dictionary """
    if player_score(hand, baseball) < player_score(hand, k_and_l):
        winner = baseball
    else:
        winner = k_and_l
    
    wilds = winner(hand)["wilds"]
    static = winner(hand)["static"]
    keys = winner(hand)["static_keys"]
    wild_cards = winner(hand)["wild_cards"]

    return {"wilds": wilds, "static":static, "static_keys":keys, "wild_cards": wild_cards}

# ====================================== HELPER FUNCTIONS ============================================================

def keys(hand):
    """ Returns cards_to_rank keys for a passed in hand list """
    keys = [cards_to_rank[x[0]] for x in hand]
    return keys

def unpack(seq):
    """ Unpacks sets for straight evaluations """
    if isinstance(seq, (list, tuple, set)):
        yield from (x for y in seq for x in unpack(y))
    elif isinstance(seq, dict):
        yield from (x for item in seq.items() for y in item for x in unpack(y))
    else:
        yield seq

def buy_fours(deck=None, player_hand=None):
    """ Allow players to buy 4s and provides options to buy again if dealt another 4."""
    fours = keys(player_hand).count(11)
    
    for x in range(0, fours):
        buy = int(input("[1]: Pay for the four \n[2]: Get it for free if you hold "))
        if buy == 1:
            deal_player(deck, player_hand, 1)
            print([player_hand[-1]])
            if keys([player_hand[-1]]) == [11]:
                second = int(input("[1]: Pay for the four \n[2]: Get it for free if you hold "))
                if second == 1:
                    deal_player(deck, player_hand, 1)
                    print([player_hand[-1]])
                    if keys([player_hand[-1]]) == [11]:
                        third = int(input("[1]: Pay for the four \n[2]: Get it for free if you hold "))
                        if third == 1:
                            deal_player(deck, player_hand, 1)
                            print([player_hand[-1]])
                            if keys([player_hand[-1]]) == [11]:
                                fourth = int(input("[1]: Pay for the four \n[2]: Get it for free if you hold "))
                                if fourth == 1:
                                    deal_player(deck, player_hand, 1)
                                    print([player_hand[-1]])
                                    
    if fours > 0:
        print(f'New Hand: {player_hand}')
    return player_hand

def player_score(hand, wild_type=None):
    """Returns a float with a players hand score. The lower the number the better the hand. Hand score is based on hand strength, then key for each of the 5 cards on a log scale. """
    player_score = float(f'{(best_hand(hand, wild_type)["strength"] * 2) + (best_hand(hand, wild_type)["top"] *.1) + (best_hand(hand, wild_type)["kicker"] *.01) + (best_hand(hand, wild_type)["kicker2"] *.001) + (best_hand(hand, wild_type)["kicker3"] *.0001) + (best_hand(hand, wild_type)["kicker4"] *.00001)}')
    return player_score

# ====================================== HAND EVALUATIONS ============================================================

def is_straight_flush(hand, wild_type=None):
    """Identifies if a straight flush exists"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]
    else:
        wilds = 0

    final_straight = None
    sf_keys = set()
    sf_value_keys = set()
    for card in hand:
        sf_keys |= sf_dict[card]
        sf_value_keys |= straight_to_ranks[card[0]]
    sf_value_keys = sorted(sf_value_keys)
    sf_keys = sorted(sf_keys)
    size = 5 - wilds

    for idx, value in enumerate(sf_keys):
        slice = sf_keys[idx:idx+size]
        if len(slice) < size:
            straight_flush = False
            break
        if set(slice).issubset(list(range(value, value+5))):
            cards = [res[card] for card in slice]
            sf_values = [straight_to_ranks[x[0]] for x in cards]
            sf_values = sorted((list(unpack(sf_values))))
            sv = max(slice[-1], 5)
            if len(slice) <5:
                    straights = straight_check(cards, None, wilds)
                    final_straight = straights()["keys"]
                    straight_flush = True
                    break
            else:
                final_straight = sf_values
                final_straight = sorted(final_straight)
                straight_flush = True
            break

        else:
            straight_flush = False
            final_straight = None                    

    return {"truthy": straight_flush, "keys": final_straight}

def straight_flush_check(hand, wild_type=None):
    """Identifies the card rank values in the straight flush"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]
    else:
        wilds = 0

    sf_keys = set()
    sf_value_keys = set()
    for card in hand:
        sf_keys |= sf_dict[card]
        sf_value_keys |= straight_to_ranks[card[0]]
    sf_value_keys = sorted(sf_value_keys)
    sf_keys = sorted(sf_keys)
    size = 5 - wilds

    for idx, value in enumerate(sf_keys):
        slice = sf_keys[idx:idx+size]
        if len(slice) < size:
            straight_flush = False
            break
        if set(slice).issubset(list(range(value, value+5))):
            straight_flush = True
            sf_showdown = [res[value] for value in slice]
            sf_values = [straight_to_ranks[x[0]] for x in sf_showdown]
            sf_values = sorted((list(unpack(sf_values))))
            break
        else:
            straight_flush = False    
    
    def straight_flush_keys():
        if straight_flush == True:
            for idx, value in enumerate(sf_values):
                slice = sf_values[idx:idx+size]
                if set(slice).issubset(list(range(value, value+5))):
                    sv = max(slice[-1], 5)
                    if len(slice) < 5:
                        missing = []
                        for i in range(sv-4,sv+1):
                                if i not in slice:
                                    missing.append(i)
                        final = slice + missing
                        final = sorted(final)
                        break
                    else:
                        final = slice
                        final = sorted(final)
                        break

            sf_cards = [value_dict[card] for card in final]
        return {"keys": final, "cards": sf_cards}
        
                
    return straight_flush_keys

def is_royal(hand, wild_type=None):
    """
    Takes in straight flush keys and checks against Royal Flush
    """
    royal_flush = False
    if is_straight_flush(hand, wild_type)["truthy"] == True:
        sf_showdown = is_straight_flush(hand, wild_type)["keys"]
        if sf_showdown[0] == 1:
            royal_flush = True
        else:
            royal_flush = False
    return royal_flush

def is_flush(hand, wild_type=None):
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]
    else:
        wilds = 0
        
    c = collections.Counter(x[1] for x in hand)
    top_suit = c.most_common(1)[0][1]
    if top_suit > (4 - wilds):
        flush = True
    else:
        flush = False
    return flush

def flush_check(hand, wild_type=None):
    """
    First class function flush_check takes a final hand and uses Counter to check for flushes
    """
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]
    else:
        wilds = 0
        
    c = collections.Counter(x[1] for x in hand)
    top_suit = c.most_common(1)[0][0]
    suit_count = c.most_common(1)[0][1]
    if suit_count > (4 - wilds):
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
        
        cards = []
        if flush == True:
            for x in hand:
                if x[1] == top_suit:
                    cards.append(x)
        return {"keys": keys, "cards": cards}
    
    return flush_keys

def is_straight(hand, wild_type=None, wilds=0):
    
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]

    keys = set()
    for card in hand:
        keys |= straight_to_ranks[card[0]]
    keys = sorted(keys)
    size = 5 - wilds

    for idx, value in enumerate(keys):
        slice = keys[idx:idx+size]
        if len(slice) < size:
            straight = False
            break
        if set(slice).issubset(list(range(value,value+5))):
            straight = True
            break
        else:
            straight = False
            
    return straight

def straight_check(hand, wild_type=None, wilds=0):
    """First class function takes final hand and checks for straight"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
        hand = wild_type(hand)["static"]

    keys = set()
    for card in hand:
        keys |= straight_to_ranks[card[0]]
    keys = sorted(keys)
    size = 5 - wilds

    for idx, value in enumerate(keys):
        slice = keys[idx:idx+size]
        if len(slice) < size:
            straight = False
            break
        if set(slice).issubset(list(range(value,value+5))):
            straight = True
            break
        else:
            straight = False
            
            
    def straight_keys():
        """Closure will identify the 5 card straight hand and return the keys"""
        if straight == True:
            sv = max(slice[-1], 5) # Identify key value of last card in straight. If it is lower than 5 set it to 5
            if len(slice) < 5: # If statc cards are less than 5 use wilds to fill gaps
                missing = []
                for i in range(sv-4,sv+1): # Uses keys to go back to a min value of 1 and adds 5 to that range then captures missing keys in that 5 card slice
                    if i not in slice:
                        missing.append(i)
                final_straight = slice + missing # Copy list item to avoid mutating original list
                final_straight = sorted(final_straight)
            else:
                final_straight = slice
                final_straight = sorted(final_straight)
                
            straight_cards = [value_dict[card] for card in final_straight]
                
            return {"keys": final_straight, "cards": straight_cards}
            
    return straight_keys 

def common_cards(hand, wild_type=None):
    """Check for common cards to be used in quads, full house, trips and pairs"""
    if wild_type != None and (len(wild_type(hand)["static"]) != 0):
        hand = wild_type(hand)["static"]
    else:
        pass
    
    card_sort = sorted(cards_to_rank[x[0]] for x in hand)
    c = collections.Counter([x for x in card_sort])   
    common = c.most_common(7)
    return common

def kickers(hand, n, wild_type=None):
    """
    n: For two-pair enter 2, for quads enter 1
    """
    if wild_type != None and (len(wild_type(hand)["static"]) != 0):
        hand = wild_type(hand)["static"]
    else:
        pass

    card_sort = sorted(cards_to_rank[x[0]] for x in hand)
    c = collections.Counter([x for x in card_sort])
    common = c.most_common(7)
    kicker_values = [x[0] for x in common[n:]]
    kickers_keys = sorted(cards_to_rank[x[0]] for x in hand if cards_to_rank[x[0]] in kicker_values)
    return sorted(kickers_keys)

def is_five_oak(hand, wild_type=None):
    """Receives the result from common_cards function to check for quads"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)
    if common_card_list[0][1] > (4 - wilds):
        five_oak = True
    else:
        five_oak = False
    return five_oak

def is_quads(hand, wild_type=None):
    """Receives the result from common_cards function to check for quads"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)
    if common_card_list[0][1] > (3 - wilds):
        quads = True
    else:
        quads = False
    return quads

def is_full_house(hand, wild_type=None):
    """Receives the result from common_cards function to check for Full House"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)    
    if common_card_list[0][1] == (3 - wilds) and common_card_list[1][1] >= 2:
        full_house = True
    else:
        full_house = False
    return full_house

def is_trips(hand, wild_type=None):
    """Receives the result from common_cards function to check for Trips"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)  
    if common_card_list[0][1] == (3 - wilds) and common_card_list[1][1] < 2:
        trips = True
    else:
        trips = False
    return trips

def is_two_pair(hand, wild_type=None):
    """Receives the result from common_cards function to check for Trips"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
            
    common_card_list = common_cards(hand, wild_type)    
    if common_card_list[0][1] == (2 - wilds) and common_card_list[1][1] == 2:
        two_pair = True
    else:
        two_pair = False
    return two_pair

def is_pair(hand, wild_type=None):
    """Receives the result from common_cards function to check for Trips"""
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)  
    if common_card_list[0][1] == (2 - wilds) and common_card_list[1][1] < 2:
        pair = True
    else:
        pair = False
    return pair

def is_high_card(hand, wild_type=None):
    if wild_type != None:
        wilds = wild_type(hand)["wilds"]
    else:
        wilds = 0
        
    common_card_list = common_cards(hand, wild_type)  
    if common_card_list[0][1] == (1 - wilds) and common_card_list[1][1] == 1:
        high_card = True
    else:
        high_card = False
    return high_card

# ====================================== BEST HAND DETERMINATION ============================================================
def best_hand(hand, wild_type=None):
    """Hand: A players final hand (hole cards plus board).
    wild_type: The wild mode of the game. Options are: low_wilds, k_and_l.
    Returns a dictionary with all aspects needed to evaluate hand winner"""
    if wild_type != None:
        wild_hand = wild_type(hand)
    else:
        wild_hand = {"wild_cards": [], "wilds": 0}
        
    if is_five_oak(hand, wild_type):
        hand_name = "Five of a Kind"
        showdown_strength = 1
        final_hand_bonus = 1000
        wilds = wild_hand["wild_cards"]
        if wild_hand["wilds"] >= 5:
            final_hand_keys = [1,1,1,1,1]
        else:
            final_hand_keys = [common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_royal(hand, wild_type):
        hand_name = "Royal Flush"
        showdown_strength = 2
        final_hand_bonus = 500
        wilds = wild_hand["wild_cards"]
        final_hand_keys = is_straight_flush(hand, wild_type)["keys"]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_straight_flush(hand, wild_type)["truthy"]:
        hand_name = "Straight Flush"
        showdown_strength = 3
        final_hand_bonus = 100
        wilds = wild_hand["wild_cards"]
        final_hand_keys = is_straight_flush(hand, wild_type)["keys"]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_quads(hand, wild_type):
        hand_name = "Quads"
        showdown_strength = 4
        final_hand_bonus = 40
        wilds = wild_hand["wild_cards"]
        final_hand_keys =[common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], min([common_cards(hand, wild_type)[1][0], common_cards(hand, wild_type)[2][0]])]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_full_house(hand, wild_type):
        hand_name= "Full House"
        showdown_strength = 5
        final_hand_bonus = 8
        wilds = wild_hand["wild_cards"]
        final_hand_keys = [common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], min(common_cards(dealer_final_hand), key = lambda t: t[1])[0], min(common_cards(dealer_final_hand), key = lambda t: t[1])[0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_flush(hand, wild_type):
        hand_name = "Flush"
        showdown_strength = 6
        final_hand_bonus = 6
        wilds = wild_hand["wild_cards"]
        flushes = flush_check(hand, wild_type)
        flush_keys = flushes()["keys"]
        flush_cards = flushes()["cards"]
        final_hand_keys = flush_keys
        for x in range(0, wild_hand["wilds"]):
            new_wild_key = (next(filterfalse(set(flush_keys).__contains__, count(1))))
            final_hand_keys.append(new_wild_key)
        final_hand_keys = sorted(final_hand_keys)
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_straight(hand, wild_type):
        hand_name = "Straight"
        showdown_strength = 7
        final_hand_bonus = 4
        wilds = wild_hand["wild_cards"]
        straights = straight_check(hand, wild_type)
        final_hand_keys = straights()["keys"]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_trips(hand, wild_type):
        hand_name = "Trips"
        showdown_strength = 8
        final_hand_bonus = 2
        wilds = wild_hand["wild_cards"]
        final_hand_keys = [common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[1][0], common_cards(hand, wild_type)[2][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_two_pair(hand, wild_type):
        hand_name = "Two Pair"
        showdown_strength = 9
        final_hand_bonus = 0
        wilds = wild_hand["wild_cards"]
        final_hand_keys =[common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[1][0], common_cards(hand, wild_type)[1][0], kickers(hand, 2, wild_type)[0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    elif is_pair(hand, wild_type):
        hand_name = "Pair"
        showdown_strength = 10
        final_hand_bonus = 0
        wilds = wild_hand["wild_cards"]
        final_hand_keys =[common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[1][0], common_cards(hand, wild_type)[2][0], common_cards(hand, wild_type)[3][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}
    else:
        hand_name = "High Card"
        showdown_strength = 11
        final_hand_bonus = 0
        wilds = wild_hand["wild_cards"]
        final_hand_keys =[common_cards(hand, wild_type)[0][0], common_cards(hand, wild_type)[1][0], common_cards(hand, wild_type)[2][0], common_cards(hand, wild_type)[3][0], common_cards(hand, wild_type)[4][0]]
        showdown_top = final_hand_keys[0]
        showdown_kicker = final_hand_keys[1] 
        showdown_kicker2 = final_hand_keys[2]
        showdown_kicker3 = final_hand_keys[3]
        showdown_kicker4 = final_hand_keys[4]
        showdown = [value_dict[showdown_top], value_dict[showdown_kicker], value_dict[showdown_kicker2], value_dict[showdown_kicker3], value_dict[showdown_kicker4]]
        return {"hand": hand_name, "strength": showdown_strength,"bonus": final_hand_bonus, "top": showdown_top, "kicker":showdown_kicker, "kicker2":showdown_kicker2, "kicker3":showdown_kicker3, "kicker4":showdown_kicker4, "showdown": showdown, "wilds": wilds}

    
# ====================================== WINNING HAND DETERMINATION ============================================================
def winning_player(player_hand, dealer_hand, wild_type=None):
    
    """Takes two hands and identifies winner"""
    player = best_hand(player_hand, wild_type)
    dealer = best_hand(dealer_hand, wild_type)
    
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