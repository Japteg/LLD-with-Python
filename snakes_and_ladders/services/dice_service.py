import random


class DiceService:

    def __init__(self, num_dices=1):
        # This supports multiple dices
        self.num_dices = num_dices

    def roll(self) -> int:
        throws = random.choices(range(1, 6), k=self.num_dices)
        return sum(throws)
