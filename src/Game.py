from Table import Table
from UIEngine import *

class Game():
    def __init__(self):
        pass

    def start_game(self):
        self.table = Table(self.determine_player_count())
        self.game_in_progress = True

        print_start_screen()

        #game loop
        while self.game_in_progress:
            self.table.start_round()
            pass

    def determine_player_count(self):
        playerCount = -1
        while (playerCount == -1):
            userResponse = input("\nHow many human players are joining the game? ")
            playerCount = self.validate_int_input(userResponse)

        return playerCount

    def validate_int_input(self, userResponse):
        try:
            userResponse = int(userResponse)
        except ValueError:
            print('Response must be an integer')
            return -1

        if (userResponse < 1 or userResponse > 5):
            print('Only a maximum of 5 players are allowed in a game')
            return -1

        return userResponse

    def promptToPlayAgain(self):
        userResponse = input("Would you like to play again? (Y/N): ")

        while (userResponse.upper() != 'Y' and userResponse.upper() != 'N'):
            userResponse = input("Invalid Reponse\nWould you like to play again? (Y/N): ")

        if userResponse.upper() == 'Y':
            start_game()
