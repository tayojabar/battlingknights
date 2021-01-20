from dataclasses import dataclass

from cell import Cell

@dataclass
class Item:

    """
        A dataclass representing the Item object

        The commented part showed that I was going to use a normal Python class, however, dealing with attributes that are non-Python objects proved difficult. 
    """

    # def __init__(self, name, value, position, attack_score, defense_score):
    #     self.name = name
    #     self.value = value
    #     self.position = position
    #     self.attack_score = attack_score
    #     self.defense_score = defense_score

    name: str
    value: int
    cell: Cell
    attack_score: int
    defense_score: int