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

    print("Round Results:")
    print("House Hand: " + house_player.hand_to_string())

    for human_player in list_of_human_players:
        formatted_stack_change = human_player.last_stack_change
        if (human_player.last_stack_change > 0):
            formatted_stack_change = "+" + str(human_player.last_stack_change)
        else:
            formatted_stack_change = str(formatted_stack_change)

        print(human_player.name + " Hand(s): " + human_player.hand_to_string() + "- Stack Change: " + formatted_stack_change)

def print_player_hands(house_player, list_of_human_players, player = False):
    row_dictionary = {
        'horizontal_border_row': VERT_BORDER,
        'label_row': VERT_BORDER,
        'card_row_1': VERT_BORDER,
        'card_row_2': VERT_BORDER,
        'card_row_3': VERT_BORDER,
        'card_row_4': VERT_BORDER
    }

    add_cards_for_hand(house_player.hands[0], HOUSE, row_dictionary)

    if player != False:
        print(player.name + '\'s turn')

    for count, human_player in enumerate(list_of_human_players):
        is_current_player = player != False and player.name == human_player.name

        label = human_player.name
        if not human_player.is_still_in_round:
            label = strike(label)

        add_cards_for_hand(human_player.hands[0], label, row_dictionary, is_current_player)

    print(row_dictionary['horizontal_border_row'])
    print(row_dictionary['label_row'])
    print(row_dictionary['horizontal_border_row'])
    print(row_dictionary['card_row_1'])
    print(row_dictionary['card_row_2'])
    print(row_dictionary['card_row_3'])
    print(row_dictionary['card_row_4'])
    print(row_dictionary['horizontal_border_row'])

def add_cards_for_hand(hand, label, row_dictionary, is_current_player = False):
    if is_current_player:
        label = '~' + label + '~'
    else:
        label = ' ' + label + ' '

    even_card_count = len(hand) % 2 == 0
    left_house_buffer_count = ceil((len(hand) - 1) * 9 / 2)
    right_house_buffer_count = left_house_buffer_count - 1 if even_card_count else left_house_buffer_count
    row_dictionary['horizontal_border_row'] += ('*' * left_house_buffer_count) + ('*' * 9) + ('*' * right_house_buffer_count)
    row_dictionary['label_row'] += (' ' * left_house_buffer_count) + label + (' ' * right_house_buffer_count)

    for card in hand:
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

    row_dictionary['horizontal_border_row'] += VERT_BORDER
    row_dictionary['label_row'] += VERT_BORDER

    row_dictionary['card_row_1'] += VERT_BORDER
    row_dictionary['card_row_2'] += VERT_BORDER
    row_dictionary['card_row_3'] += VERT_BORDER
    row_dictionary['card_row_4'] += VERT_BORDER

# TODO: make a version that actually works in this console.
def strike(text):
    return text
    # result = ''
    # for c in text:
    #     result = result + c + '\u0336'
    # return result