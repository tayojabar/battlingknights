from dataclasses import dataclass

from item import Item
from cell import Cell

@dataclass
class Knight:

    """
        A dataclass representing the Knight object

        The commented part showed that I was going to use a normal Python class, however, dealing with attributes that are non-Python objects proved difficult. 
    """

    # def __init__(self, id, color, position, status='LIVE', equipped, attack_score = 1, defense_score = 1):
    #     self.id = id
    #     self.color = color
    #     self.position = position
    #     self.status = status
    #     self.equipped = equipped
    #     self.attack_score = attack_score
    #     self.defense_score = defense_score

    id: str
    color: str
    cell: Cell
    status: str = 'LIVE' #default status LIVE
    equipped: Item = None
    base_attack_score: int = 1
    base_defense_score: int = 1