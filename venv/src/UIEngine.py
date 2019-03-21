from math import ceil

TAB = "         "
HOUSE = " House "
HUMAN = "Human "
HORIZONTAL_BORDER_SECTION = "*************************"
VERT_BORDER = "*"


def print_start_screen():
    print("\nWelcome to Blackjack")


def print_new_round():
    print("\nStarting new round")


def round_results(house_player, list_of_human_players):
    print_player_hands(house_player, list_of_human_players)

    print("\nRound Results:")
    print("House Hand: " + house_player.hand_to_string())

    for human_player in list_of_human_players:
        formatted_stack_change = human_player.last_stack_change
        if human_player.last_stack_change > 0:
            formatted_stack_change = "+" + str(human_player.last_stack_change)
        else:
            formatted_stack_change = str(formatted_stack_change)

        print(human_player.name + " Hand(s): " + human_player.hand_to_string() + "- Stack Change: " + formatted_stack_change)


def print_player_hands(house_player, list_of_human_players, player=False):
    row_dictionary = {
        'horizontal_border_row': VERT_BORDER,
        'label_row': VERT_BORDER,

        'hand_1_label_row': VERT_BORDER,
        'hand_2_label_row': VERT_BORDER,
        'card_row_1': VERT_BORDER,
        'card_row_2': VERT_BORDER,
        'card_row_3': VERT_BORDER,
        'card_row_4': VERT_BORDER,
    }
    add_spacing_dependent_on_hand(HOUSE, row_dictionary, len(house_player.hands[0]))
    add_cards_for_hand(house_player.hands[0], row_dictionary, len(house_player.hands[0]))

    multiple_hands = False

    for count, human_player in enumerate(list_of_human_players):
        if len(human_player.hands) > 1:
            multiple_hands = True

        is_current_player = player != False and player.name == human_player.name

        max_cards = get_max_cards(human_player)

        add_spacing_dependent_on_hand(human_player.name, row_dictionary, max_cards, is_current_player)
        add_cards_for_hand(human_player.hands[0], row_dictionary, max_cards, is_current_player)

    print()
    if player != False:
        print(player.name + '\'s turn')

    print(row_dictionary['horizontal_border_row'])
    print(row_dictionary['label_row'])
    print(row_dictionary['horizontal_border_row'])

    if multiple_hands:
        print(row_dictionary['hand_1_label_row'])

    print(row_dictionary['card_row_1'])
    print(row_dictionary['card_row_2'])
    print(row_dictionary['card_row_3'])
    print(row_dictionary['card_row_4'])

    if multiple_hands:
        row_dictionary['card_row_1'] = VERT_BORDER
        row_dictionary['card_row_2'] = VERT_BORDER
        row_dictionary['card_row_3'] = VERT_BORDER
        row_dictionary['card_row_4'] = VERT_BORDER

        add_cards_for_hand([], row_dictionary, len(house_player.hands[0]))

        for count, human_player in enumerate(list_of_human_players):
            is_current_player = player != False and player.name == human_player.name
            add_cards_for_hand(human_player.hands[1] if len(human_player.hands) > 1 else [],
                               row_dictionary, get_max_cards(human_player), is_current_player)

        print(row_dictionary['hand_2_label_row'])
        print(row_dictionary['card_row_1'])
        print(row_dictionary['card_row_2'])
        print(row_dictionary['card_row_3'])
        print(row_dictionary['card_row_4'])

    print(row_dictionary['horizontal_border_row'])


def get_max_cards(human_player):
    return len(human_player.hands[1]) if len(human_player.hands) > 1 and len(human_player.hands[1]) > len(
        human_player.hands[0]) else len(human_player.hands[0])


def add_cards_for_hand(hand, row_dictionary, max_cards, is_current_player=False):
    for count in range(max_cards):
        if count >= len(hand):
            row_dictionary['card_row_1'] += "         "
            row_dictionary['card_row_2'] += "         "
            row_dictionary['card_row_3'] += "         "
            row_dictionary['card_row_4'] += "         "
        else:
            card = hand[count]
            row_dictionary['card_row_1'] += "  *****  "
            if card[1] or is_current_player:
                if card[0][0] == '10':
                    row_dictionary['card_row_2'] += "  *" + card[0][0] + " *  "
                else:
                    row_dictionary['card_row_2'] += "  *" + card[0][0] + "  *  "
                row_dictionary['card_row_3'] += "  *  " + card[0][1] + "*  "
            else:
                row_dictionary['card_row_2'] += "  *****  "
                row_dictionary['card_row_3'] += "  *****  "
            row_dictionary['card_row_4'] += "  *****  "

    row_dictionary['card_row_1'] += VERT_BORDER
    row_dictionary['card_row_2'] += VERT_BORDER
    row_dictionary['card_row_3'] += VERT_BORDER
    row_dictionary['card_row_4'] += VERT_BORDER


def add_spacing_dependent_on_hand(label, row_dictionary, max_cards, is_current_player=False):
    if is_current_player:
        label = '~' + label + '~'
    else:
        label = ' ' + label + ' '

    even_card_count = max_cards % 2 == 0
    left_house_buffer_count = ceil((max_cards - 1) * 9 / 2)
    right_house_buffer_count = left_house_buffer_count - 1 if even_card_count else left_house_buffer_count
    row_dictionary['horizontal_border_row'] += ('*' * left_house_buffer_count) + ('*' * 9) + ('*' * right_house_buffer_count)
    row_dictionary['label_row'] += (' ' * left_house_buffer_count) + label + (' ' * right_house_buffer_count)

    row_dictionary['hand_1_label_row'] += (' ' * left_house_buffer_count) + '  Hand 1 ' + (' ' * right_house_buffer_count)
    row_dictionary['hand_2_label_row'] += (' ' * left_house_buffer_count) + '  Hand 2 ' + (' ' * right_house_buffer_count)

    row_dictionary['horizontal_border_row'] += VERT_BORDER
    row_dictionary['label_row'] += VERT_BORDER
    row_dictionary['hand_1_label_row'] += VERT_BORDER
    row_dictionary['hand_2_label_row'] += VERT_BORDER


