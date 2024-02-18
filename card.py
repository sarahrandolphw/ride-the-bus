class Card:
    suits = {0: "clubs", 1: "hearts", 2: "diamonds", 3: "spades"}
    ranks = {2: "Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",
             10:"Ten", 11:"Jack", 12:"Queen", 13:"King", 14: "Ace"}

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def string(self) -> str:
        #a card is 2 ints, so it takes the ints and maps them to their string value and prints
        return str(self.ranks.get(self.rank)) + " of " + str(self.suits.get(self.suit))

    # def check_red_black(self, target) -> bool:
    #     if self.suit == 0 or self.suit == 3:
    #         return target.suit == 0 or self.suit == 3
    #     return target.suit == 1 or target.suit == 2


