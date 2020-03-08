import operator
import collections
import random
wins = 0
losses = 0
pushes = 0
hole_wins = 0
final_wins = 0
rounds = 0

def test():
    # Initialize Deck
    deck = {1: 'Ah', 2: 'Kh', 3: 'Qh', 4: 'Jh', 5: 'Th', 6: '9h', 7: '8h', 8: '7h',
        9: '6h', 10: '5h', 11: '4h', 12: '3h', 13: '2h', 14: 'Ad', 15: 'Kd', 16: 'Qd', 17: 'Jd', 18: 'Td',
        19: '9d', 20: '8d', 21: '7d', 22: '6d', 23: '5d', 24: '4d', 25: '3d', 26: '2d', 27: 'Ac', 28: 'Kc', 29: 'Qc', 
        30: 'Jc', 31: 'Tc', 32: '9c', 33: '8c', 34: '7c', 35:'6c', 36:'5c', 37:'4c', 38:'3c', 39:'2c', 40:'As', 41:'Ks',
        42: 'Qs', 43:'Js', 44:'Ts', 45:'9s', 46:'8s', 47:'7s', 48:'6s', 49:'5s', 50:'4s', 51:'3s',52:'2s'}

    # Hole Bonus check for pocket pairs
    pair_bonus = {'A': 21, 'K': 9, 'Q': 9, 'J':9, 'T':4, '9':4, '8':4, '7':4, '6':4, '5':3,'4':3,'3':3,'2':3}

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


    # Declare Player Hand
    player_hand = []
    for x in range(2):
        player_hand.append(deck.pop(random.choice(list(deck.keys()))))    
    print(f'Player Has: {player_hand}')


    dealer_hand = []
    for x in range(2):
        dealer_hand.append(deck.pop(random.choice(list(deck.keys()))))    
    print(f'Dealer Has: {dealer_hand}')

    board = []
    for x in range(5):
        board.append(deck.pop(random.choice(list(deck.keys()))))    
    print(board)

    suited = player_hand[0][1] == player_hand[1][1]

    if ((player_hand[0] == 'Ad') or (player_hand[0] == 'Ah')) and ((player_hand[1] == 'Ah') or (player_hand[1] == 'Ad')):
        hole_bonus_payout = 51
        print(f' RED ACES!!! Pays {hole_bonus_payout - 1}:1')
    elif ((player_hand[0][0] == 'A') and (player_hand[1][0] == 'K')) or ((player_hand[0][0] == 'K') and (player_hand[1][0] == 'A')):
        if suited == True:
            hole_bonus_payout = 26
            print(f' Big Slick!! Pays {hole_bonus_payout - 1}:1')
        else:
            hole_bonus_payout = 0
            print("Sorry, Bonus Bet Lost")
    elif player_hand[0][0] == player_hand[1][0]:
        pair = player_hand[0][0]
        hole_bonus_payout = pair_bonus[player_hand[0][0]]
        print(f'Pocket {pair}s! Pays {hole_bonus_payout - 1}:1')
    elif suited == True:
        hole_bonus_payout = 2
        print(f'Suited! Pays {hole_bonus_payout - 1}:1')
    else:
        hole_bonus_payout = 0
        print("Sorry, Bonus Bet Lost")

    final_hand = player_hand + board
    d_final_hand = dealer_hand + board

    # Key Value of final hand cards appended to list in order of frequency then value
    final_hand_keys = [cards_to_rank[x[0]] for x in final_hand]
    counts = collections.Counter(final_hand_keys)
    final_hand_keys = sorted(final_hand_keys, key=lambda x: (counts[x], -x), reverse=True)
    final_hand_keys

    # Strip suits from cards and set values to a list
    pairs = []
    for card in final_hand:
        pairs.append(card[0])

    # Capture the numeric value associated with each key
    pair_keys = list()
    for card in pairs:
        pair_keys.append(cards_to_rank[card])

    # Create lists for each hand rank, populated with appropriate keys which will assist in evaluating final hand
    qk = []
    fh = []
    tk = []
    pk = []
    hc = []

    # Set Booleans for hand value to False before flipping to True when appropriate in upcoming loops
    royal_flush = False
    straight_flush = False
    quads = False
    full_house = False
    flush = False
    straight = False
    trips = False
    two_pair = False
    pair = False
    high_card = False

    # Royal Flush and Straight Flush Check
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
                straight_flush_top_key = value
                if straight_flush_top_key == 1:
                    royal_flush = True
                    straight_flush_top = value_dict[value]
                    straight_flush_string = (f'ROYAL FLUSH!!!')
                    straight_flush_showdown = [value_dict[value] for value in slice]
                    break
                else:
                    royal_flush = False
                    straight_flush_top = value_dict[value]
                    straight_flush_string = (f'Straight Flush to the {straight_flush_top}')
                    straight_flush_showdown = [value_dict[value] for value in slice]
                    break

    # FLUSH CHECK
    # Check for flush
    suits = []
    for x in final_hand:
        suits.append(x[1])

    if (suits.count('s') >= 5) or (suits.count('c') >= 5) or (suits.count('d') >= 5) or (suits.count('h') >= 5):
        flush = True
    else:
        flush = False

    # If there is a flush, seperate those cards into their own list
    if flush == True:
        spades = []
        clubs = []
        hearts = []
        diamonds = []
        flush_hand = []
        flush_string = []
        for card in final_hand:
            if card[1] == 'c':
                clubs.append(card)
            if card[1] == 's':
                spades.append(card)
            if card[1] == 'd':
                diamonds.append(card)
            if card[1] == 'h':
                hearts.append(card)
        all_suits = [spades, diamonds, hearts, clubs]
        for x in all_suits:
            if len(x) > 4:
                for idx, value in x:
                    flush_hand.append(cards_to_rank[idx])        
        flush_hand = sorted(flush_hand)
        flush_hand = flush_hand[0:5]
        flush_showdown = [value_dict[x] for x in flush_hand]

    # Straight Check
    keys = set()
    for card in final_hand:
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
            straight_string = (f'Straight to the {straight_top}')
            straight_showdown = [value_dict[value] for value in slice]
            break
        else:
            straight = False
            

    # Capture frequency counts of each key and append those values to their appropriate lists. Run first level hand assignment
    for idx, value in enumerate(pair_keys):
        if pair_keys.count(value) > 3:
            quads = True
            qk.append(value)
            qk = list(dict.fromkeys(qk))
            qk = sorted(qk) 
            quad_top = qk[0]
        elif pair_keys.count(value) == 3:
            trips = True
            tk.append(value)
            tk = list(dict.fromkeys(tk))
            tk = sorted(tk)
            trip_top = tk[0]
        elif pair_keys.count(value) == 2:
            pair = True
            pk.append(value)
            pk = list(dict.fromkeys(pk))
            pk = sorted(pk)
        elif pair_keys.count(value) == 1:
            hc.append(value)
            hc = list(dict.fromkeys(hc))
            hc = sorted(hc)

    # If trips is true, check for full house
    if trips == True:
        if len(tk) > 1:
            full_house = True
            fh_top = tk[0]
            fh_bottom = tk[1]
            fh.append(fh_bottom)
            fh_string = (f'Full House {value_dict[fh_top]}s over {value_dict[fh_bottom]}s')
        elif pair == True:
            full_house = True
            fh_top = tk[0]
            fh_bottom = pk[0]
            fh.append(fh_bottom)
            fh_string = (f'Full House {value_dict[fh_top]}s over {value_dict[fh_bottom]}s')      
        else:
            full_house = False
            tk_top = tk[0]

    # If pair is true, check for two pair, ignore when there is a Full House
    if pair == True and straight != True and flush != True and full_house != True and quads != True and straight_flush != True:
        if len(pk) > 1:
            two_pair = True
            tp_top = pk[0]
            tp_bottom = pk[1]
        else:
            two_pair = False
            p_top = pk[0]
        
    if two_pair != True and trips != True and full_house != True and quads != True and straight != True and flush != True:
        hc_top = hc[0]
        hc1 = value_dict[hc_top]
        hc_two = hc[1]
        hc2 = value_dict[hc_two]
        hc_three = hc[2]
        hc3 = value_dict[hc_three]
        hc_four = hc[3]
        hc4 = value_dict[hc_four]
        hc_five = hc[4]
        hc5 = value_dict[hc_five]
        
    if pair != True and two_pair != True and trips != True and straight != True and flush != True and full_house != True and quads != True:
        high_card = True
        
    # showdown_strength variable will be used to quickly compare player hand to dealer hand to evaluate winner
    showdown_kicker = 99
    showdown_kicker_2 = 99
    showdown_kicker_3 = 99
    showdown_kicker_4 = 99


    if royal_flush == True:
        showdown = sf_showdown
        showdown_string = straight_flush_string
        showdown_top = straight_flush_top_key
        showdown_kicker = straight_flush_top_key
        showdown_strength = 1
        hand = "Royal Flush"
        final_hand_bonus = 501
    elif straight_flush == True:
        showdown = sf_showdown
        showdown_string = straight_flush_string
        showdown_top = straight_flush_top_key
        showdown_kicker = straight_flush_top_key
        showdown_strength = 2
        hand = "Straight Flush"
        final_hand_bonus = 101
    elif quads == True:
        showdown_top = quad_top
        showdown_string = (f'Quad {showdown_top}s with a {value_dict[final_hand_keys[4]]} Kicker')
        showdown_kicker = final_hand_keys[4]
        showdown = [value_dict[quad_top], value_dict[quad_top], value_dict[quad_top], value_dict[quad_top], value_dict[showdown_kicker]]
        showdown_strength = 3
        hand = "Quads"
        final_hand_bonus = 41
    elif full_house == True:
        showdown = [value_dict[fh_top], value_dict[fh_top], value_dict[fh_top], value_dict[fh_bottom], value_dict[fh_bottom]]
        showdown_string = fh_string
        showdown_top = fh_top
        showdown_kicker = fh_bottom
        showdown_strength = 4
        hand = "Full House"
        final_hand_bonus = 9
    elif flush == True:
        showdown = flush_showdown
        showdown_string = (f'{flush_showdown[0]} high flush!')
        showdown_top = flush_hand[0]
        showdown_kicker = flush_hand[1]
        showdown_kicker_2 = flush_hand[2]
        showdown_kicker_3 = flush_hand[3]
        showdown_kicker_4 = flush_hand[4]
        showdown_strength = 5
        hand = "Flush"
        final_hand_bonus = 7
    elif straight == True:
        showdown = straight_showdown
        showdown_string = straight_string
        showdown_top = straight_top_key
        showdown_kicker = straight_top_key 
        showdown_strength = 6
        hand = "Straight"
        final_hand_bonus = 5
    elif trips == True:
        showdown_top = trip_top
        showdown_kicker = final_hand_keys[3]
        showdown_kicker_2 = final_hand_keys[4]
        showdown = [value_dict[trip_top], value_dict[trip_top], value_dict[trip_top], value_dict[showdown_kicker], value_dict[showdown_kicker_2]]
        showdown_string = (f'Trip {value_dict[trip_top]} with {value_dict[showdown_kicker]} and {value_dict[showdown_kicker_2]} as kickers')
        showdown_strength = 7
        hand = "Trips"
        final_hand_bonus = 3
    elif two_pair == True:
        showdown_top = tp_top
        showdown_kicker = tp_bottom
        showdown_kicker_2 = final_hand_keys[4]
        showdown = [value_dict[tp_top], value_dict[tp_top], value_dict[tp_bottom], value_dict[tp_bottom], value_dict[showdown_kicker_2]]
        showdown_string = (f'Two Pair {value_dict[tp_top]}s and {value_dict[tp_bottom]}s with a(n) {value_dict[showdown_kicker_2]}')
        showdown_strength = 8
        hand = "Two Pair"
        final_hand_bonus = 0
    elif pair == True:
        showdown = [value_dict[p_top],value_dict[p_top], hc1, hc2, hc3]
        showdown_string = (f'Pair of {value_dict[p_top]}s with a {hc1} kicker')
        showdown_top = p_top
        showdown_kicker = hc_top
        showdown_kicker_2 = hc_two
        showdown_kicker_3 = hc_three
        showdown_strength = 9
        hand = "Pair"
        final_hand_bonus = 0
    elif high_card == True:
        showdown = [hc1, hc2, hc3, hc4, hc5]
        showdown_string = (f'{hc1} High, {hc2} kicker')
        showdown_top = hc_top
        showdown_kicker = hc_two   
        showdown_kicker_2 = hc_three
        showdown_kicker_3 = hc_four
        showdown_kicker_4 = hc_five
        showdown_strength = 10
        hand = "High Card"
        final_hand_bonus = 0

    # Key Value of final hand cards appended to list in order of frequency then value
    d_final_hand_keys = [cards_to_rank[x[0]] for x in d_final_hand]
    counts = collections.Counter(d_final_hand_keys)
    d_final_hand_keys = sorted(d_final_hand_keys, key=lambda x: (counts[x], -x), reverse=True)

    # Strip suits from cards and set values to a list
    d_pairs = []
    for card in d_final_hand:
        d_pairs.append(card[0])

    # Capture the numeric value associated with each key
    d_pair_keys = list()
    for card in d_pairs:
        d_pair_keys.append(cards_to_rank[card])

    # Create lists for each hand rank, populated with appropriate keys which will assist in evaluating final hand
    d_qk = []
    d_fh = []
    d_tk = []
    d_pk = []
    d_hc = []

    # Set Booleans for hand value to False before flipping to True when appropriate in upcoming loops
    d_royal_flush = False
    d_straight_flush = False
    d_quads = False
    d_full_house = False
    d_flush = False
    d_straight = False
    d_trips = False
    d_two_pair = False
    d_pair = False
    d_high_card = False

    # Royal Flush and Straight Flush Check
    d_sf_keys = set()
    d_sf_value_keys = set()
    for card in d_final_hand:
        d_sf_keys |= sf_dict[card]
        d_sf_value_keys |= straight_to_ranks[card[0]]
    d_sf_value_keys = sorted(d_sf_value_keys)
    d_sf_keys = sorted(d_sf_keys)

    for idx, value in enumerate(d_sf_keys):
        slice = d_sf_keys[idx:idx+5]
        if len(slice) < 5:
            d_straight_flush = False
            break
        if slice == list(range(value,value+5)):
            d_straight_flush = True
            d_sf_showdown = [res[value] for value in slice]
            break
        else:
            d_straight_flush = False
            
            
    if d_straight_flush == True:
        for idx, value in enumerate(d_sf_value_keys):
            slice = d_sf_value_keys[idx:idx+5]
            if slice == list(range(value,value+5)):
                d_straight_flush_top_key = value
                if d_straight_flush_top_key == 1:
                    d_royal_flush = True
                    d_straight_flush_top = value_dict[value]
                    d_straight_flush_string = (f'ROYAL FLUSH!!!')
                    d_straight_flush_showdown = [value_dict[value] for value in slice]
                    break
                else:
                    d_royal_flush = False
                    d_straight_flush_top = value_dict[value]
                    d_straight_flush_string = (f'Straight Flush to the {d_straight_flush_top}')
                    d_straight_flush_showdown = [value_dict[value] for value in slice]
                    break

    # FLUSH CHECK
    # Check for flush
    d_suits = []
    for x in d_final_hand:
        d_suits.append(x[1])

    if (d_suits.count('s') >= 5) or (d_suits.count('c') >= 5) or (d_suits.count('d') >= 5) or (d_suits.count('h') >= 5):
        d_flush = True
    else:
        d_flush = False

    # If there is a flush, seperate those cards into their own list
    if d_flush == True:
        d_spades = []
        d_clubs = []
        d_hearts = []
        d_diamonds = []
        d_flush_hand = []
        d_flush_string = []
        for card in d_final_hand:
            if card[1] == 'c':
                d_clubs.append(card)
            if card[1] == 's':
                d_spades.append(card)
            if card[1] == 'd':
                d_diamonds.append(card)
            if card[1] == 'h':
                d_hearts.append(card)
        d_all_suits = [d_spades, d_diamonds, d_hearts, d_clubs]
        for x in d_all_suits:
            if len(x) > 4:
                for idx, value in x:
                    d_flush_hand.append(cards_to_rank[idx])        
        d_flush_hand = sorted(d_flush_hand)
        d_flush_hand = d_flush_hand[0:5]
        d_flush_showdown = [value_dict[x] for x in d_flush_hand]

    # Straight Check
    d_keys = set()
    for card in d_final_hand:
        d_keys |= straight_to_ranks[card[0]]
    d_keys = sorted(d_keys)

    for idx, value in enumerate(d_keys):
        slice = d_keys[idx:idx+5]
        if len(slice) < 5:
            d_straight = False
            break
        if slice == list(range(value,value+5)):
            d_straight = True
            d_straight_top_key = value
            d_straight_top = value_dict[value]
            d_straight_string = (f'Straight to the {d_straight_top}')
            d_straight_showdown = [value_dict[value] for value in slice]
            break
        else:
            d_straight = False
            

    # Capture frequency counts of each key and append those values to their appropriate lists. Run first level hand assignment
    for idx, value in enumerate(d_pair_keys):
        if d_pair_keys.count(value) > 3:
            d_quads = True
            d_qk.append(value)
            d_qk = list(dict.fromkeys(d_qk))
            d_qk = sorted(d_qk) 
            d_quad_top = d_qk[0]
        elif d_pair_keys.count(value) == 3:
            d_trips = True
            d_tk.append(value)
            d_tk = list(dict.fromkeys(d_tk))
            d_tk = sorted(d_tk)
            d_trip_top = d_tk[0]
        elif d_pair_keys.count(value) == 2:
            d_pair = True
            d_pk.append(value)
            d_pk = list(dict.fromkeys(d_pk))
            d_pk = sorted(d_pk)
        elif d_pair_keys.count(value) == 1:
            d_hc.append(value)
            d_hc = list(dict.fromkeys(d_hc))
            d_hc = sorted(d_hc)


    # If trips is true, check for full house
    if d_trips == True:
        if len(d_tk) > 1:
            d_full_house = True
            d_fh_top = d_tk[0]
            d_fh_bottom = d_tk[1]
            d_fh.append(d_fh_bottom)
            d_fh_string = (f'Full House {value_dict[d_fh_top]}s over {value_dict[d_fh_bottom]}s')
        elif d_pair == True:
            d_full_house = True
            d_fh_top = d_tk[0]
            d_fh_bottom = d_pk[0]
            d_fh.append(d_fh_bottom)
            d_fh_string = (f'Full House {value_dict[d_fh_top]}s over {value_dict[d_fh_bottom]}s')       
        else:
            d_full_house = False
            d_tk_top = d_tk[0]

    # If pair is true, check for two pair, ignore when there is a Full House
    if d_pair == True and d_straight != True and d_flush != True and d_full_house != True and d_quads != True and d_straight_flush != True:
        if len(d_pk) > 1:
            d_two_pair = True
            d_tp_top = d_pk[0]
            d_tp_bottom = d_pk[1]
        else:
            d_two_pair = False
            d_p_top = d_pk[0]
        
    if d_two_pair != True and d_trips != True and d_full_house != True and d_quads != True and d_straight != True and d_flush != True:
        d_hc_top = d_hc[0]
        d_hc1 = value_dict[d_hc_top]
        d_hc_two = d_hc[1]
        d_hc2 = value_dict[d_hc_two]
        d_hc_three = d_hc[2]
        d_hc3 = value_dict[d_hc_three]
        d_hc_four = d_hc[3]
        d_hc4 = value_dict[d_hc_four]
        d_hc_five = d_hc[4]
        d_hc5 = value_dict[d_hc_five]
        
    if d_pair != True and d_two_pair != True and d_trips != True and d_straight != True and d_flush != True and d_full_house != True and d_quads != True:
        d_high_card = True

    # showdown_strength variable will be used to quickly compare player hand to dealer hand to evaluate winner
    d_showdown_kicker = 99
    d_showdown_kicker_2 = 99
    d_showdown_kicker_3 = 99
    d_showdown_kicker_4 = 99


    if d_royal_flush == True:
        d_showdown = d_sf_showdown
        d_showdown_string = d_straight_flush_string
        d_showdown_top = d_straight_flush_top_key
        d_showdown_kicker = d_straight_flush_top_key
        d_showdown_strength = 1
        d_hand = "Royal Flush"
        d_final_hand_bonus = 501
    elif d_straight_flush == True:
        d_showdown = d_sf_showdown
        d_showdown_string = d_straight_flush_string
        d_showdown_top = d_straight_flush_top_key
        d_showdown_kicker = d_straight_flush_top_key
        d_showdown_strength = 2
        d_hand = "Straight Flush"
        d_final_hand_bonus = 101
    elif d_quads == True:
        d_showdown_top = d_quad_top
        d_showdown_string = (f'Quad {d_showdown_top}s with a {value_dict[d_final_hand_keys[4]]} Kicker')
        d_showdown_kicker = d_final_hand_keys[4]
        d_showdown = [value_dict[d_quad_top], value_dict[d_quad_top], value_dict[d_quad_top], value_dict[d_quad_top], value_dict[d_showdown_kicker]]
        d_showdown_strength = 3
        d_hand = "Quads"
        d_final_hand_bonus = 41
    elif d_full_house == True:
        d_showdown = [value_dict[d_fh_top], value_dict[d_fh_top], value_dict[d_fh_top], value_dict[d_fh_bottom], value_dict[d_fh_bottom]]
        d_showdown_string = d_fh_string
        d_showdown_top = d_fh_top
        d_showdown_kicker = d_fh_bottom
        d_showdown_strength = 4
        d_hand = "Full House"
        d_final_hand_bonus = 9
    elif d_flush == True:
        d_showdown = d_flush_showdown
        d_showdown_string = (f'{d_flush_showdown[0]} high flush!')
        d_showdown_top = d_flush_hand[0]
        d_showdown_kicker = d_flush_hand[1]
        d_showdown_kicker_2 = d_flush_hand[2]
        d_showdown_kicker_3 = d_flush_hand[3]
        d_showdown_kicker_4 = d_flush_hand[4]
        d_showdown_strength = 5
        d_hand = "Flush"
        d_final_hand_bonus = 7
    elif d_straight == True:
        d_showdown = d_straight_showdown
        d_showdown_string = d_straight_string
        d_showdown_top = d_straight_top_key
        d_showdown_kicker = d_straight_top_key 
        d_showdown_strength = 6
        d_hand = "Straight"
        d_final_hand_bonus = 5
    elif d_trips == True:
        d_showdown_top = d_trip_top
        d_showdown_kicker = d_final_hand_keys[3]
        d_showdown_kicker_2 = d_final_hand_keys[4]
        d_showdown = [value_dict[d_trip_top], value_dict[d_trip_top], value_dict[d_trip_top], value_dict[d_showdown_kicker], value_dict[d_showdown_kicker_2]]
        d_showdown_string = (f'Trip {value_dict[d_trip_top]} with {value_dict[d_showdown_kicker]} and {value_dict[d_showdown_kicker_2]} as kickers')
        d_showdown_strength = 7
        d_hand = "Trips"
        d_final_hand_bonus = 3
    elif d_two_pair == True:
        d_showdown_top = d_tp_top
        d_showdown_kicker = d_tp_bottom
        d_showdown_kicker_2 = d_final_hand_keys[4]
        d_showdown = [value_dict[d_tp_top], value_dict[d_tp_top], value_dict[d_tp_bottom], value_dict[d_tp_bottom], value_dict[d_showdown_kicker_2]]
        d_showdown_string = (f'Two Pair {value_dict[d_tp_top]}s and {value_dict[d_tp_bottom]}s with a(n) {value_dict[d_showdown_kicker_2]}')
        d_showdown_strength = 8
        d_hand = "Two Pair"
        d_final_hand_bonus = 0
    elif d_pair == True:
        d_showdown = [value_dict[d_p_top],value_dict[d_p_top], d_hc1, d_hc2, d_hc3]
        d_showdown_string = (f'Pair of {value_dict[d_p_top]}s with a {d_hc1} kicker')
        d_showdown_top = d_p_top
        d_showdown_kicker = d_hc_top
        d_showdown_kicker_2 = d_hc_two
        d_showdown_kicker_3 = d_hc_three
        d_showdown_strength = 9
        d_hand = "Pair"
        d_final_hand_bonus = 0
    elif d_high_card == True:
        d_showdown = [d_hc1, d_hc2, d_hc3, d_hc4, d_hc5]
        d_showdown_string = (f'{d_hc1} High, {d_hc2} kicker')
        d_showdown_top = d_hc_top
        d_showdown_kicker = d_hc_two   
        d_showdown_kicker_2 = d_hc_three
        d_showdown_kicker_3 = d_hc_four
        d_showdown_kicker_4 = d_hc_five
        d_showdown_strength = 10
        d_hand = "High Card"
        d_final_hand_bonus = 0

    def player_win_string():
        print(f'Player Wins with {showdown_string}')
        print(f'Dealer had {d_showdown_string}')
        pass

    def dealer_win_string():
        print(f'Dealer Wins with {d_showdown_string}')
        print(f'Player had {showdown_string}')
        pass

    push = False

    if showdown_strength < d_showdown_strength:
        winner = True
    elif showdown_strength > d_showdown_strength:
        winner = False
    elif showdown_strength == d_showdown_strength:
        if showdown_top < d_showdown_top:
            winner = True
        elif showdown_top > d_showdown_top:
            winner = False
        elif showdown_top == d_showdown_top:    
            if showdown_kicker < d_showdown_kicker:
                winner = True
            elif showdown_kicker > d_showdown_kicker:
                winner = False
            elif showdown_kicker == d_showdown_kicker:
                    if showdown_kicker_2 < d_showdown_kicker_2:
                        winner = True
                    elif showdown_kicker_2 > d_showdown_kicker_2:
                        winner = False
                    elif showdown_kicker_2 == d_showdown_kicker_2:
                                    if showdown_kicker_3 < d_showdown_kicker_3:
                                        winner = True
                                    elif showdown_kicker_3 > d_showdown_kicker_3:
                                        winner = False
                                    elif showdown_kicker_3 == d_showdown_kicker_3:
                                        if showdown_kicker_4 < d_showdown_kicker_4:
                                            winner = True
                                        elif showdown_kicker_4 > d_showdown_kicker_4:
                                            winner = False
                                        else:
                                            push = True

    else:
        print("This should never print")

    global wins
    global losses 
    global pushes 

    if push == True:
        print("Push")
        pushes +=1
    elif winner == True:
        player_win_string()
        wins +=1
    elif winner == False:
        dealer_win_string()
        losses +=1
    else:
        print("Something broke. Call the Floor")

    if final_hand_bonus > 0:
        print(f'{hand}: Pays {final_hand_bonus}:1')

    print('--------------------------------')


    
    global hole_wins
    hole_wins += hole_bonus_payout
    global final_wins
    final_wins += final_hand_bonus
    global rounds
    rounds += 1

for i in range(0,20000):
    test()

print(f'{rounds} Rounds')
print(f'Wins: {wins}')
print(f'Losses: {losses}')
print(f'Pushes: {pushes}')
print(f'Hole Bonus Units: {hole_wins}')
print(f'Final Hand Bonus Units: {final_wins}')
print('--------------------------------')
print(f'Normal Wagered: ${rounds*40}')
print(f'Normal Results: ${(wins*80) + pushes*40}')
print(f'Hole Bonus Wager: ${rounds*10}')
print(f'Hole Bonus Results ${hole_wins*10}')
print(f'Final Bonus Wager: ${rounds*10}')
print(f'Final Bonus Results ${final_wins*10}')
print(f'Total Profit/Loss ${((pushes*40)+(wins*80)+(hole_wins*10)+(final_wins*10)) - ((rounds*40)+(rounds*10)+(rounds*10))}')