from models.snake import Snake
from models.ladder import Ladder
from models.player import Player


class InputParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.snakes = []
        self.players = []
        self.ladders = []

    def parse(self):
        with open(self.file_name, 'r') as file:
            # Snakes input
            num_snakes = int(file.readline())
            for _ in range(num_snakes):
                row = file.readline()
                row = row.rstrip('\n').split(' ')
                head = int(row[0])
                tail = int(row[1])
                self.snakes.append(Snake(head, tail))
            # Ladders input
            num_ladders = int(file.readline())
            for _ in range(num_ladders):
                row = file.readline()
                row = row.rstrip('\n').split(' ')
                start = int(row[0])
                end = int(row[1])
                self.ladders.append(Ladder(start, end))
            # Players input
            num_players = int(file.readline())
            for _ in range(num_players):
                row = file.readline()
                row = row.rstrip('\n').split(' ')
                player_name = row[0]
                self.players.append(Player(player_name))

            result = {
                'players': self.players,
                'ladders': self.ladders,
                'snakes': self.snakes
            }

            return result
