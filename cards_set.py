class CardsSet:
    def __init__(self):
        self.cards = [0] * 7

    def add(self, other: 'CardsSet'):
        self.cards = [x + y for x, y in zip(self.cards, other.cards)]

    def add_card(self, card: int):
        self.cards[card] += 1
