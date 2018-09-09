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


# Populate the deck with 52 card objects
deck = []


def populate():
    for i in range(1, 5):
        for j in range(1, 14):
            deck.append(Card(j, i))


populate()

# Deals five cards to player 1 and player 2
p1_hand = []
p2_hand = []


def deal(x):
    print("Your hand is:")
    for i in range(x):
        p1_hand.append(deck.pop(0))
        p2_hand.append(deck.pop(0))
        print(
            f"{p1_hand[i].translate_rank()} of {p1_hand[i].translate_suit()}")

# Reveals the top # cards of the deck


print("""
      Welcome to Five Card Stud! Your options are:
      showdown - evaluate the winner of the game
      deal - deal five cards to yourself an your opponent
      shuffle - randomize the deck
      peek # - output # cards of cards from the top of the deck
      """)

choice = input(">")

if choice == "shuffle":
    shuffle(deck)
elif choice == "deal":
    deal(5)

print('stop')
print('no really')

# elif choice == "peek":
#     for i in range(5):
