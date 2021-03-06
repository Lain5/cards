from random import shuffle
from collections import defaultdict

class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        assert 1 <= rank <= 13, "Invalid Rank"
        assert 1 <= suit <= 4, "Invalid Suit"

    def translate_rank(self):
        rank_dict = {1: "2",
                     2: "3",
                     3: "4",
                     4: "5",
                     5: "6",
                     6: "7",
                     7: "8",
                     8: "9",
                     9: "Ten",
                     10: "Jack",
                     11: "Queen",
                     12: "King",
                     13: "Ace"}

        return rank_dict[self.rank]

    def translate_suit(self):
        suit_dict = {1: "Spades",
                     2: "Hearts",
                     3: "Diamonds",
                     4: "Clubs"}

        return suit_dict[self.suit]


# Populate the deck with 52 card objects and shuffles them
deck = []
p1_hand = []
p2_hand = []

def populate():
    for i in range(1, 5):
        for j in range(1, 14):
            deck.append(Card(j, i))

populate()
shuffle(deck)

# Deals five cards to player 1 and player 2

def deal(x):
    print("Your hand is...")
    for i in range(x):
        p1_hand.append(deck.pop(0))
        print(
            f"{p1_hand[i].translate_rank()} of {p1_hand[i].translate_suit()}")
    print("\n")

    print("Your opponent's hand is...")
    for i in range(x):
        p2_hand.append(deck.pop(0))
        print(
            f"{p2_hand[i].translate_rank()} of {p2_hand[i].translate_suit()}")

deal(5)

# Straight Flush: checks to see if the hand clears the tests for both straight and flush

def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

# Quads: Uses the defaultdict object to count the number of instances of each rank in the hand. If you have 4x of one rank, True.

def check_quads(hand):
    ranks = []
    for i in range(len(hand)): 
        ranks.append(hand[i].rank)
    rank_count = defaultdict(int)
    for j in ranks:
        rank_count[j] += 1
    if sorted(rank_count.values()) == [1,4]:
        return True
    return False
    
# Full House: Uses the defaultdict object to count the number of instances of each rank in the hand. If you have 3x of one rank and 2x of another, True.

def check_boat(hand):
    ranks = []
    for i in range(len(hand)): 
        ranks.append(hand[i].rank)
    rank_count = defaultdict(int)
    for j in ranks:
        rank_count[j] += 1
    if sorted(rank_count.values()) == [2,3]:
        return True
    return False

# checks to see if the hand is a value by adding the suit of each card in the hand to a set (which only accepts unique values). 
# If length of set = 1, flush = true.

def check_flush(hand):
    suits = set()
    for i in range(len(hand)):
        suits.add(hand[i].suit)
    if len(suits) == 1:
        return True
    else:
        return False

# checks to see if the hand is a straight by adding the rank of each card in the set to a list, which is sorted in ascending order.
# if the value of the rank of the highest card - the lowest card = 4, then straight = true

def check_straight(hand):
    ranks = []
    for i in range(len(hand)):
        ranks.append(hand[i].rank)
    ranks.sort()
    if ranks[4] - ranks[0] == 4:
        return True
    else:
# checks for the wheel
        if ranks == [1,2,3,4,13]:
            return True
        return False

# Trips: Uses the defaultdict object to count the number of instances of each rank in the hand. If you have 3x of one rank and 1x of two other ranks, True.

def check_trips(hand):
    ranks = []
    for i in range(len(hand)): 
        ranks.append(hand[i].rank)
    rank_count = defaultdict(int)
    for j in ranks:
        rank_count[j] += 1
    if sorted(rank_count.values()) == [1,1,3]:
        return True
    return False

# Two Pair: Uses the defaultdict object to count the number of instances of each rank in the hand. If you have 2x of one rank and 2x of another, True.

def check_two_pair(hand):
    ranks = []
    for i in range(len(hand)): 
        ranks.append(hand[i].rank)
    rank_count = defaultdict(int)
    for j in ranks:
        rank_count[j] += 1
    if sorted(rank_count.values()) == [1,2,2]:
        return True
    return False

# One Pair: Uses the defaultdict object to count the number of instances of each rank in the hand. If you have 2x of one rank and 3 others, True.

def check_one_pair(hand):
    ranks = []
    for i in range(len(hand)): 
        ranks.append(hand[i].rank)
    rank_count = defaultdict(int)
    for j in ranks:
        rank_count[j] += 1
    if sorted(rank_count.values()) == [1,1,1,2]:
        return True
    return False

def assign_hand_classification(hand):
    if check_straight_flush(hand):
        return 9
    if check_quads(hand):
        return 8
    if check_boat(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_straight(hand):
        return 5
    if check_trips(hand):
        return 4
    if check_two_pair(hand):
        return 3
    if check_one_pair(hand):
        return 2
    else:
        return 1

print(assign_hand_classification(p1_hand))
print(assign_hand_classification(p2_hand))

#     then
#     establish strength within hand classification

#     then
#     compare the strength of the two players
    
#     then
#     print the hand classification of player 1 and player 2, and declare winner based on strength