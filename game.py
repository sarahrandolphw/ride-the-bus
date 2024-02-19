from card import Card
from deck import Deck
from guess import Guess
from hand import Hand
import time
class Game:

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._hands = []
        self._current_player = 0
        self._current_guess_type = 0

    def _set_player_num(self):
        print('welcome to ride the bus!')
        while True:
            try:
                self._num_players = int(input('enter the number of players\n'))
                if self._num_players < 1 or self._num_players > 6:
                    print('needs to be an integer 1-6\n')
                else:
                    # print('game created with', self._num_players, 'players')
                    return
            except ValueError:
                print('needs to be an integer 1-6')
    def _set_player_hands(self):
        for player in range(self._num_players):
            string = 'player ' + str(player + 1)+ '\'s name: '
            name = input(string)
            self._hands.append(Hand(name))
        print('')
        # print for debugging
        # for hand in self._hands:
        #     print(hand.string())

    def _take_guess(self, hand: Hand, guess_type: int) -> int:
        guess = None
        while True:
            try:
                if guess_type == 0:
                    print('')
                    guess = int(input(f'{hand.get_player()}: red(1) or black(2)?\n'))
                    if 1 <= guess <= 2:
                        return guess
                    else:
                        print('must be (1) or (2)')
                elif guess_type == 1:
                    guess = int(input(f'{hand.get_player()}: over(1) or under(2)?\n'))
                    if 1 <= guess <= 2:
                        return guess
                    else:
                        print('must be (1) or (2)')
                elif guess_type == 2:
                    guess = int(input(f'{hand.get_player()}: inside(1) or outside(2)?\n'))
                    if 1 <= guess <= 2:
                        return guess
                    else:
                        print('must be (1) or (2)')
                elif guess_type == 3:
                    guess = int(input(f'{hand.get_player()}: suit?\nclubs(1) hearts(2) diamonds(3) spades(4)\n'))
                    if 1 <= guess <= 4:
                        return guess
                    else:
                        print('must be (1) (2) (3) or (4)')
            except ValueError:
                print('guess must be a number')

                #TODO: fix no copy pase for first 3
    #scan for which user is playing a card, verify the input, call play card to modify the hand, return updated hand?
    #might be a better way to split this
    def _take_card_play(self, hand: Hand, curr_card: Card): #calling update hand should update the object regardless of returning
        target = curr_card.rank #only the # of the card matters for this round
        while True:
            try:
                pass
            except ValueError:
                print('input must be an integer')

    def _verify_play_card(self, target: int, player_idx: int) -> bool:
        hand = self._hands[player_idx]
        cards = hand.get_cards()
        nums = []
        for card in cards:
            nums.append(card.rank)
        return target in nums

    def _handle_checker(self, result: bool):
        if result is False:
            print('drink')
        else:
            print('nice')
        #this should probably be in another function but works here for now
        # print('enter to continue')
        # input()
        time.sleep(1)
    def play(self):
        self._set_player_num()
        self._set_player_hands()
        # curr_card = self._deck.draw()
        # input_guess = self._take_guess(self._hands[self._current_player], self._current_guess_type)
        # curr_guess_obj = Guess(input_guess, curr_card, self._current_guess_type, self._hands[self._current_player])
        # result = curr_guess_obj.check_red_black()
        # self._handle_checker(result)
        # print(curr_card.string())
        for round_idx in range(0, 4):
            for player_idx in range(0,self._num_players):
                curr_card = self._deck.draw()
                if round_idx != 0:
                    print(self._hands[player_idx].string())
                input_guess = self._take_guess(self._hands[player_idx], round_idx)
                curr_guess_obj = Guess(input_guess, curr_card, round_idx,
                                        self._hands[player_idx])
                curr_hand = self._hands[player_idx]
                curr_hand.add_card(curr_card)
                if round_idx == 0:
                    result = curr_guess_obj.check_red_black()
                elif round_idx == 1:
                    result = curr_guess_obj.check_over_under()
                elif round_idx == 2:
                    result = curr_guess_obj.check_inbetween()
                elif round_idx == 3:
                    result = curr_guess_obj.check_suit()
                print(curr_card.string())
                self._handle_checker(result)
        #^^THIS IS THE PART OF THE GAME WHERE EVERYONE GETS THEIR HAND NOW WE PLAY
        curr_round = 1
        for i in range(0,3):
            curr_card = self._deck.draw()
            for player_idx in range(0, self._num_players):
                print(self._hands[player_idx].string())
            #maybe add another method for this
            print('current card:', curr_card.string(), '\nwould anyone like to play their card?\nNone: (0)')
            player_buttons = ''
            for player in range(0, self._num_players):
                player_buttons += self._hands[player].get_player() + ': (' + str(player + 1) + ')\n'
            try:
                player_card_down = int(input(player_buttons)) - 1 #adjust for players indexing at 0 but buttons start at 1
            except ValueError:
                print('pass')




if __name__ == '__main__':
    game = Game()
    game.play()
