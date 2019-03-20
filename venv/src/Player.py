from Utilities import get_value_of_card

class Player():

    def __init__(self, human_player = False, name = "House", stack_amount = 500):
        self.human_player = human_player
        self.stack_amount = stack_amount
        self.name = name

        # Hands to an array of 1-2 sets of cards. Each card is a Dictionary
        # with denomination and visibility
        self.hands = []
        self.bet = 0
        self.is_still_in_round = False
        self.last_stack_change = 0

    def check_split_eligability(self):
        return self.hands[0][0][0] == self.hands[0][1][0]

    def check_double_eligability(self):
        first_card_value = get_value_of_card(self.hands[0][0][0][0])
        second_card_value = get_value_of_card(self.hands[0][1][0][0])

        if first_card_value == 1:
            first_card_value = 1
        elif second_card_value == 1:
            second_card_value = 1

        return sum == 9 or sum == 10 or sum == 11

    def bust_player(self, stack_change = 0):
        self.is_still_in_round = False
        for hand in self.hands:
            for card in hand:
                print(card)
                print(card[1])
                card[1] = True
        self.stack_amount += stack_change
        self.last_stack_change = stack_change
        print('LOG: Player is being removed from game: ' + self.name)

    def hand_to_string(self):
        hand_string = ""
        for hand in self.hands:
            hand_string += "{ "
            for card in hand:
                hand_string += card[0][0] + card[0][1] + " "
            hand_string += "} "

        return hand_string

    def round_reset(self):
        self.is_still_in_round = True
        self.hands = []
        self.bet = 0