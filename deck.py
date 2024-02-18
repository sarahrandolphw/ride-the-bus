from card import Card
import random
class Deck:

    def __init__(self):
        self.deck = []
        for i in range(0,4):
            for j in range(2, 15): #mapped 2 - 15 in hashmap in card.py
                self.deck.append(Card(j, i))

    def print_deck(self):
        for card in self.deck:
            print(card.string())

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self) -> Card:
        return self.deck.pop(0)

# if __name__ == '__main__':
#     deck = Deck()
#     deck.print_deck()
#     deck.shuffle()
#     deck.print_deck()
#     card = deck.draw()
#     print(card.string())

