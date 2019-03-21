import random


class BlackjackDeck:

    def __init__(self):
        SPADES = "\u2660"
        HEARTS = "\u2665"
        DIAMONDS = "\u2666"
        CLUBS = "\u2663"
        self.deck_template = [
            ('A', HEARTS), ('A', DIAMONDS), ('A', SPADES), ('A', CLUBS),
            ('K', HEARTS), ('K', DIAMONDS), ('K', SPADES), ('K', CLUBS),
            ('Q', HEARTS), ('Q', DIAMONDS), ('Q', SPADES), ('Q', CLUBS),
            ('J', HEARTS), ('J', DIAMONDS), ('J', SPADES), ('J', CLUBS),
            ('10', HEARTS), ('10', DIAMONDS), ('10', SPADES), ('10', CLUBS),
            ('9', HEARTS), ('9', DIAMONDS), ('9', SPADES), ('9', CLUBS),
            ('8', HEARTS), ('8', DIAMONDS), ('8', SPADES), ('8', CLUBS),
            ('7', HEARTS), ('7', DIAMONDS), ('7', SPADES), ('7', CLUBS),
            ('6', HEARTS), ('6', DIAMONDS), ('6', SPADES), ('6', CLUBS),
            ('5', HEARTS), ('5', DIAMONDS), ('5', SPADES), ('5', CLUBS),
            ('4', HEARTS), ('4', DIAMONDS), ('4', SPADES), ('4', CLUBS),
            ('3', HEARTS), ('3', DIAMONDS), ('3', SPADES), ('3', CLUBS),
            ('2', HEARTS), ('2', DIAMONDS), ('2', SPADES), ('2', CLUBS),
        ]

        self.build_new_deck()

    def draw_card(self):
        return self.deck.pop(0)

    def is_past_reshuffle(self):
        return len(self.deck) <= 65

    def build_new_deck(self, number_of_decks_included = 4):
        self.deck = []
        self.number_of_decks_included = number_of_decks_included

        for num in range(number_of_decks_included):
            self.deck.extend(self.deck_template)

        random.shuffle(self.deck)

    def reshuffle(self):
        if (self.number_of_decks_included < 1):
            self.build_new_deck()
        else:
            self.build_new_deck(self.number_of_decks_included)
