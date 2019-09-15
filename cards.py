from random import shuffle


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
#shuffle(deck)

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

def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

def check_quads(hand):
    ranks = {1:0, 
             2:0,
             3:0,
             4:0,
             5:0, 
             6:0,
             7:0,
             8:0,
             9:0,
             10:0,
             11:0,
             12:0,
             13:0}
             
    for i in range(1,14):
        for j in range (0,5):
            if hand[j].rank == i:
                ranks[j] += 1
    print(ranks)
    
check_quads(p1_hand)

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
        return False

print(check_straight_flush(p1_hand))


# def evaluate(hand):
#     if 
#     straight flush
#     if
#     quads
#     if
#     full house
#     if
#     flush
#     if
#     straight
#     if
#     trips
#     if
#     two pair
#     if
#     one pair
#     if 
#     high card

#     then
#     establish strength within hand classification

#     then
#     compare the strength of the two players
    
#     then
#     print the hand classification of player 1 and player 2, and declare winner based on strength