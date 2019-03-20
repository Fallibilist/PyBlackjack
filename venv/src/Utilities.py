# Utilities
def get_value_of_card(card_denomination):
    # Find a way to handle this better
    value_template = {
        'A': 1,
        'K': 10,
        'Q': 10,
        'J': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }
    return value_template[card_denomination]