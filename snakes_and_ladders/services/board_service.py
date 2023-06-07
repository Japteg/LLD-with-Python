from typing import List
from models.board import GameBoard
from models.snake import Snake
from models.ladder import Ladder
from models.player import Player
from .board_service_interface import BoardServiceInterface


class BoardService(BoardServiceInterface):

    def __init__(self):
        self.board = None

    def initialize_board(self, snakes: List[Snake], ladders: List[Ladder],
                         players: List[Player], size=100):
        self.board = GameBoard()
        self.board.set_size(size)
        # Set snake positions on board
        snake_pos = {}
        for snake in snakes:
            snake_pos[snake.get_head()] = snake
        self.board.set_snakes(snake_pos)
        # Set ladder positions on board
        ladder_pos = {}
        for ladder in ladders:
            ladder_pos[ladder.get_start()] = ladder
        self.board.set_ladders(ladder_pos)
        # initially all players are at 0 position on board
        player_pieces = {}
        for player in players:
            player_pieces[player] = 0
        self.board.set_player_pieces(player_pieces)

    def update_player_piece(self, player, dice_throw):
        curr_pos = self.board.player_pieces[player]
        new_pos = curr_pos
        if self.valid_move(curr_pos, dice_throw):
            new_pos = curr_pos + dice_throw
            new_pos = self.check_snake_bite(new_pos)
            new_pos = self.check_ladder_climb(new_pos)
            # Update player piece on board
            self.set_player_piece(player, new_pos)
            
        print(f'{player.get_name()} rolled a {dice_throw} and moved from '
              f'{curr_pos} to {new_pos}')

    def set_player_piece(self, player, pos):
        """
        Sets new player position on board
        """
        self.board.player_pieces[player] = pos

    def valid_move(self, pos, dice_throw) -> bool:
        """
        Check if move is possible
        """
        return pos + dice_throw <= self.board.get_size()

    def check_snake_bite(self, pos) -> int:
        """
        :return: new position
        """
        # Check if snake is present at this position
        if pos in self.board.get_snakes().keys():
            return self.board.get_snakes()[pos].get_tail()
        return pos

    def check_ladder_climb(self, pos) -> int:
        """
        :return: new position
        """
        # Check if ladder is present at this position
        if pos in self.board.get_ladders().keys():
            return self.board.get_ladders()[pos].get_end()
        return pos

    def check_winner(self, player):
        """
        Check if this player has won
        """
        player_pieces = self.board.get_player_pieces()
        return player_pieces[player] == self.board.get_size()
