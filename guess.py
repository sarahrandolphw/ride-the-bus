from card import Card
from hand import Hand
class Guess:

    guess_types = ['color','over under', 'inbetween', 'suit']

    def __init__(self, guess: int, curr_card: Card, type: int, hand: Hand = None):
        self._guess = guess
        self._curr_card = curr_card
        self._hand = hand
        self._type = type

    #1 for red 2 for black: 2 possibilities for guess
    def check_red_black(self) -> bool:
        if self._guess == 1 and (self._curr_card.suit == 1 or self._curr_card.suit == 2):
            return True
        if self._guess == 2 and (self._curr_card.suit == 0 or self._curr_card.suit == 3):
            return True
        return False

    def check_over_under(self) -> bool:
        target = self._hand.get_cards()[0].rank
        curr = self._curr_card.rank
        if curr > target:
            return self._guess == 1
        if curr < target:
            return self._guess == 2
        return False

    def check_inbetween(self) -> bool:
        nums = [self._hand.get_cards()[0].rank, self._hand.get_cards()[1].rank]
        nums.sort()
        curr = self._curr_card.rank
        if nums[0] < curr < nums[1]:
            return self._guess == 1 #inside
        if curr < nums[0] or curr > nums[1]:
            return self._guess == 2 #outside
        return False

    def check_suit(self) -> bool:
        target = self._curr_card.suit + 1 #suits index at 0, player guesses at 1
        guess = self._guess
        return target == guess
    #1 for under 2 for over
    # def check_over_under(self) -> bool:
    #     card = self._hand.get(0).rank
    #     if self._guess == 1 and

