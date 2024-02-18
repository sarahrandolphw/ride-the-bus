from card import Card
from deck import Deck
class Hand:
    def __init__(self, player: str):
        self._player = player
        self._cards = []

    def get_cards(self) -> list:
        return self._cards

    def add_card(self, card: Card):
        self._cards.append(card)

    def play_card(self, card: Card) -> Card:
        self._cards.remove(card)
        return card

    def get_player(self) -> str:
        return self._player

    def string(self) -> str:
        string = str(self._player) + '\'s hand:\n'
        # print(self._player.strip(), "'s hand:") #.strip() removes trailing space
        for card in self._cards:
            string += card.string() + '\n'
        return string



# if __name__ == '__main__':
#     deck = Deck()
#     deck.shuffle()
#     card1 = deck.draw()
#     card2 = deck.draw()
#     hand = Hand('sarah')
#     hand.add_card(card1)
#     hand.add_card(card2)
#     print(hand.string())
#     hand.play_card(card1)
#     print(hand.string())


