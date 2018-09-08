# import random


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        assert rank in range(1, 13), "Invalid Rank"
        assert suit in range(1, 4), "Invalid Suit"

    def translate(self):
        rank_dict = {1: "2",
                     2: "3",
                     3: "4",
                     4: "5",
                     5: "6",
                     6: "7",
                     7: "8",
                     8: "9",
                     9: "T",
                     10: "J",
                     11: "Q",
                     12: "K",
                     13: "A"}

        suit_dict = {1: "s",
                     2: "h",
                     3: "d",
                     4: "c"}

        return rank_dict[self.rank], suit_dict[self.suit]


variable = Card(2, 2)

testr, tests = variable.translate()
