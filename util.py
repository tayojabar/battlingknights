from pathlib import Path
from json import dumps

from pprint import pprint

class Utils: 
    @staticmethod
    def read_moves():
        """ A helper fuction to read the moves.txt file"""
        stream = Path('./moves.txt').read_text()
        lines = stream.strip().split('\n')
        #The following pop operations are there in the assumption that the first and last lines are GAME-START and GAME-END respectively.
        lines.pop(0)
        lines.pop()
        return (tuple(tuple(move.split(':')) for move in lines))

    @staticmethod
    def save_game(knights = [], items = []):
        """ A helper fuction to save the final states of the knights and items. Also prepares the jsonified results the moves.txt file"""
        final_state = {}

        for knight in knights:
            if knight.cell:
                final_position = knight.cell.to_json()
            else:
                final_position = None
            knight_state = (final_position, knight.status)

            if knight.equipped:
                knight_state += (
                            knight.equipped.name,
                            knight.base_attack_score + knight.equipped.attack_score,
                            knight.base_defense_score + knight.equipped.defense_score
                        )
            else:
                knight_state += (
                            None, knight.base_attack_score, knight.base_defense_score
                        )   
            final_state[knight.color] = knight_state

        for item in items:
            final_position = item.cell.to_json()
            if item.cell.knight:
                held = True
            else:
                held = False
            item_state = (final_position, held)
            final_state[item.name] = item_state
        
        pprint (final_state)
        return final_state
    
    @staticmethod
    def write_to_file(final_state):
        """Helper function to write final game state to file. Purely for separation of concerns."""
        Path('./final_state.json').write_text(dumps(final_state))

