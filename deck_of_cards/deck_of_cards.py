import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:

    def __init__(self):
        self.cards = []
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else :
            raise ValueError("Only full decks can be shuffled")
        return self.cards

    def deal_card(self):
        return self.cards.pop()

    def deal_hand(self, count):
        return self._deal(count)

    def _deal(self, count):
        cards = []
        for x in range(0, count):
            if len(self.cards) == 0:
                raise ValueError("All cards have been dealt")
            else:
                cards.append(self.cards.pop())

        return cards

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'



deck_one = Deck()

# Should return 52
print(deck_one.count())
# Should return all cards
print(deck_one.shuffle())
# Should return one card
print(deck_one.deal_card())
# Should return 51
print(deck_one.count())
# Should return a set of cards
print(deck_one.deal_hand(5))
# Should return "Deck of 51-x Cards"
print(deck_one.__repr__())

# Should return Error "Only full decks can be shuffled"
# print(deck_one.shuffle())
# Should return Error "All cards dealt"
#print(deck_one.deal_hand(50))
