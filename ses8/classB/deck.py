"""
implement the:

 __len__         method
 __add__         method
 __repr__        method
 __str__         method
 __setitem__     method
 __delitem__     method
"""


class Deck:
    def __init__(self, cards):
        self.__cards = cards
   
    @property
    def cards(self):
        return self.__cards

    def __add__(self, other):
        return Deck(self.cards + other.cards)


    def __getitem__(self, key):
        return self.__cards[key]

    def __setitem__(self, key, val):
        self.__cards[key] = val
   
    def __delitem__(self, key):
        del(self.__cards[key])


    def __len__(self):
        return len(self.__cards)

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return 'Cards in deck: ' + str(self.cards)
