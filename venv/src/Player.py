from Utilities import get_value_of_card


class Player:

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
        self.eliminated_split_hand_index = -1

    def check_split_eligability(self):
        return self.hands[0][0][0][0] == self.hands[0][1][0][0]

    def check_double_eligability(self):
        if len(self.hands) > 1:
            return False

        first_card_value = get_value_of_card(self.hands[0][0][0][0])
        second_card_value = get_value_of_card(self.hands[0][1][0][0])

        card_sum = first_card_value + second_card_value

        return card_sum == 9 or card_sum == 10 or card_sum == 11

    def bust_player(self, stack_change = 0, hand_index = -1):
        if len(self.hands) == 1:
            for hand in self.hands:
                for card in hand:
                    card[1] = True
            self.is_still_in_round = False
            self.stack_amount += stack_change
            self.last_stack_change = stack_change

        else:
            if self.eliminated_split_hand_index != -1:
                self.is_still_in_round = False

            self.eliminated_split_hand_index = hand_index

            for card in self.hands[hand_index]:
                card[1] = True

            self.stack_amount += stack_change / 2
            self.last_stack_change += stack_change / 2

        if stack_change > 0:
            print(self.name + " has been paid out $" + str(stack_change) + "\n")
        elif stack_change < 0:
            print(self.name + " has been deducted $" + str(stack_change) + "\n")

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
        self.last_stack_change = 0
        self.eliminated_split_hand_index = -1
