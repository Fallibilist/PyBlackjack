from Player import Player
from BlackjackDeck import BlackjackDeck
from Utilities import get_value_of_card
from UIEngine import *

class Table():

    def __init__(self, number_of_human_players=1):

        self.house_player = Player()
        self.list_of_human_players = []

        for num in range(number_of_human_players):
            self.list_of_human_players.append(Player(True, "Human " + str(num + 1)))

        # Initialize decks
        self.deck = BlackjackDeck()

    def start_round(self):
        self.round_reset()
        print_new_round()

        self.player_bets()
        self.deal_to_players()

        print_player_hands(self.house_player, self.list_of_human_players)

        # Check for Blackjacks
        house_naturaled = self.check_for_natural(self.house_player)
        if house_naturaled:
            print('LOG: House naturaled!')
            # Todo move below
            for hand in self.house_player.hands:
                for card in hand:
                    card[1] = True

        for human_player in self.list_of_human_players:
            if self.check_for_natural(human_player):
                # User has natural
                if house_naturaled:
                    # player gets their bet back
                    human_player.bust_player()
                else:
                    # get 1.5x they bet, and their bet back
                    human_player.bust_player(human_player.bet * 1.5)
            else:
                if house_naturaled:
                    # player loses bet and is eliminated from round
                    human_player.bust_player(-human_player.bet)

        if self.get_remaining_players() >= 2:
            for human_player in self.list_of_human_players:
                if human_player.is_still_in_round:
                    # Check if they can split or double down
                    if human_player.check_split_eligability():
                        self.prompt_player_to_split(human_player);
                        pass

                    if human_player.check_double_eligability():
                        self.prompt_player_to_double_down(human_player);
                        pass

                    # Prompt to hit, stay
                    self.prompt_user_to_act_and_check_bust(human_player)

            # Once it gets to the House they make their decision based on a formula
            if self.get_remaining_players() >= 2:
                print('LOG: House is about to act since players remain')
                self.prompt_house_to_act()

                if self.house_player.is_still_in_round:
                    house_hand_total = self.calculate_hand_total(self.house_player.hands[0])

                    for human_player in self.list_of_human_players:
                        if human_player.is_still_in_round:
                            for hand in human_player.hands:
                                player_hand_total = self.calculate_hand_total(hand)
                                if player_hand_total < house_hand_total:
                                    human_player.bust_player(-human_player.bet)
                                elif player_hand_total > house_hand_total:
                                    human_player.bust_player(human_player.bet)
                                else:
                                    human_player.bust_player()
                    self.house_player.bust_player()
                else:
                    for human_player in self.list_of_human_players:
                        if human_player.is_still_in_round:
                            # Notify them of the win
                            human_player.bust_player(human_player.bet)

        round_results(self.house_player, self.list_of_human_players)

        # Check if we are past the reshuffle point. If so reset decks
        if self.deck.is_past_reshuffle():
            self.deck.reshuffle()

    def prompt_house_to_act(self):
        first_card = get_value_of_card(self.house_player.hands[0][0][0][0])
        second_card = get_value_of_card(self.house_player.hands[0][1][0][0])
        min_hand_value = first_card + second_card
        has_ace = first_card == 1 or second_card == 1

        while (min_hand_value < 17):
            if has_ace and min_hand_value + 10 <= 21 and min_hand_value + 10 >= 17:
                min_hand_value += 10
                break

            new_card = self.deck.draw_card()
            self.house_player.hands[0].append([new_card, True])
            min_hand_value += get_value_of_card(new_card[0])
            if new_card[0] == 1:
                has_ace = True

        if (min_hand_value > 21):
            self.house_player.bust_player()

    # Returns true if the user busts
    def prompt_user_to_act_and_check_bust(self, player):
        print_player_hands(self.house_player, self.list_of_human_players, player)

        for hand in player.hands:
            first_card = get_value_of_card(hand[0][0][0])
            second_card = get_value_of_card(hand[1][0][0])
            min_hand_value = first_card + second_card

            while (min_hand_value <= 21):
                string_value = str(min_hand_value)
                if ((first_card == 1 or second_card == 1) and (min_hand_value + 10) <= 21):
                    string_value += '/' + str(min_hand_value + 10)

                print('Current hand value: ' + string_value)
                user_response = input('Would you like to hit or stay? (H or S): ')
                while (user_response.upper() != 'H' and user_response.upper() != 'S'):
                    user_response = input("Invalid Reponse\nWould you like to hit or stay? (H or S): ")

                if user_response.upper() == 'H':
                    # Draw card
                    new_card = self.deck.draw_card()
                    hand.append([new_card, True])
                    min_hand_value += get_value_of_card(new_card[0])
                    if min_hand_value > 21:
                        player.bust_player(-player.bet)
                else:
                    return

    def get_remaining_players(self):
        remaining_players = 0

        if self.house_player.is_still_in_round:
            remaining_players += 1

        for human_player in self.list_of_human_players:
            if human_player.is_still_in_round:
                remaining_players += 1

        return remaining_players

    def player_bets(self):
        for count, human_player in enumerate(self.list_of_human_players):
            if human_player.stack_amount < 2:
                print('You do not have enough for the minimum bet! You will be removed.')
                human_player.bust_player()
            else:
                self.prompt_user_to_bet(human_player)

    def prompt_user_to_bet(self, human_player):
        human_player.bet = 0
        while (human_player.bet < 2):
            userResponse = input(
                "\n(" + human_player.name + ") Enter a bet from $2-" + str(human_player.stack_amount) + ": ")
            human_player.bet = self.validate_bet(userResponse, human_player.stack_amount)

        human_player.is_still_in_round = True

    def validate_bet(self, userResponse, max_bet):
        try:
            userResponse = float(userResponse)
        except ValueError:
            print('Response must be an number')
            return 0

        if userResponse < 2:
            print('The minimum bet is $2')
            return 0
        if userResponse > max_bet:
            print('You only have $' + str(max_bet))
            return 0

        return userResponse

    def deal_to_players(self):
        self.house_player.hands.clear()
        self.house_player.hands.append([[self.deck.draw_card(), False], [self.deck.draw_card(), True]])

        for human_player in self.list_of_human_players:
            human_player.hands.clear()
            human_player.hands.append([[self.deck.draw_card(), False], [self.deck.draw_card(), True]])

    def check_for_natural(self, player):
        min_hand_value = 0
        ace = False

        for card in player.hands[0]:
            card_value = get_value_of_card(card[0][0])
            if card_value == 1:
                ace = True
            min_hand_value += card_value

        return min_hand_value == 21 or (ace and min_hand_value + 10 == 21)

    def round_reset(self):
        self.house_player.round_reset()

        for human_player in self.list_of_human_players:
            human_player.round_reset()

    def calculate_hand_total(self, hand):
        min_hand_value = 0
        ace = False

        for card in hand:
            card_value = get_value_of_card(card[0][0])
            if card_value == 1:
                ace = True
            min_hand_value += card_value

    def prompt_player_to_split(self, human_player):
        user_response = input("Would you like to split? (Y/N): ")

        while (user_response.upper() != 'Y' and user_response.upper() != 'N'):
            user_response = input("Invalid Reponse\nWould you like to split? (Y/N): ")

        if (user_response.upper() == 'Y'):
            pass

    def prompt_player_to_double_down(self):
        pass

