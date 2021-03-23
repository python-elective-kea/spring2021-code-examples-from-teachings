
class Deck:
    def __init__(self):
        self.__cards = ['A', 'K', 4, 7]
    
    def __repr__(self):
        return f'{self.__dict__}'

    def __getitem__(self, key):
        return self.__cards[key]

    def __len__(self):
        return len(self.__cards)

