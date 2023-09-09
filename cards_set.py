from typing import List


class CardsSet:
    def __init__(self):
        self.cards = [0] * 7

    def __str__(self):
        return str([i for i, j in enumerate(self.cards) for _ in range(j)])

    def add(self, other: 'CardsSet'):
        self.cards = [x + y for x, y in zip(self.cards, other.cards)]

    def remove(self, other: 'CardsSet'):
        self.cards = [x - y for x, y in zip(self.cards, other.cards)]

    def add_card(self, card: int):
        self.cards[card] += 1

    def select(self, n: int) -> List['CardsSet']:
        result = []
        self._backtrack(result, CardsSet(), 0, n)
        return result

    def clone(self) -> 'CardsSet':
        new_cards_set = CardsSet()
        new_cards_set.add(self)
        return new_cards_set

    def _backtrack(self, result: List['CardsSet'], current: 'CardsSet', start: int, total: int):
        if total == 0:
            result.append(current.clone())
        elif start < len(self.cards):
            if self.cards[start] > 0:
                self.cards[start] -= 1
                current.cards[start] += 1
                self._backtrack(result, current, start, total - 1)
                current.cards[start] -= 1
                self.cards[start] += 1
            self._backtrack(result, current, start + 1, total)
