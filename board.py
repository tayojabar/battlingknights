from dataclasses import dataclass
from operator import attrgetter

from cell import Cell


"""
    I left the commented code so that my thought process could be pictured.
"""

class Board:
    
    STATUS = ['LIVE', 'DEAD', 'DROWNED']

    def __init__(self):
        """
            This sets the squares (cells) on the board. An initialization
        """
        board = []
        for x in range(0,8):
            column = [Cell(x, y) for y in range(0,8)]
            board.append(tuple(column))

        self.board = tuple(board)

    def move(self, knight, direction):
        """
            1. Knight movements are simulated here.
            2. The exception checks for drowning. 
            3. The first condition in the else statement checks if there is a knight on the cell already, 
                prompting a battle if that is the case
            4. The second and third conditions assert that there's no knight on the cell and appropriately check for the items instead. 
                The knight is equipped accoringly as specified in the instructions.
        """
        print (knight)
        knight.cell.knight = None
        try: 
            new_cell = self.change_position(knight.cell, direction)
            print (new_cell.knight)
            print ("New Cell: ", new_cell, "\n")

        except:
            item, position = self.kill_knight(knight, 2)

            # item = knight.equipped
            # last_pos = knight.cell
            # knight.status = 'DROWNED'
            # knight.cell = None
            # knight.equipped = None
            # knight.base_attack = 0
            # knight.base_defence = 0

            if item:
                item.cell = position
                position.items.append(item)
                position.items.sort(key=attrgetter('value'))

        else: 
            print ("Defender: ", new_cell.knight)
            if (new_cell.knight is not None):
                print ("BATTLE")
                winner, loser = self.attack(knight, new_cell.knight)
                print ("Winner: ", winner)
                print ("Loser: ", loser ,"\n")

                winner.cell = new_cell
                new_cell.knight = winner
                if winner.equipped:
                    winner.equipped.cell = new_cell
                item, position = self.kill_knight(loser, 1)
                # item_ = loser.equipped
                # last_pos = loser.cell
                # loser.status = "DEAD"
                # loser.cell = None
                # loser.equipped = None
                # loser.attack_score = 0
                # loser.defense_score = 0

                if item:
                    item.cell = position
                    position.items.append(item)
                    position.items.sort(key=attrgetter('value'))

                return winner
            
            if (new_cell.knight is None and len(new_cell.items) == 0):
                knight.cell = new_cell
                new_cell.knight = knight
                if knight.equipped:
                    knight.equipped.cell = new_cell

            elif (len(new_cell.items) > 0):
                knight.cell = new_cell
                new_cell.knight = knight
                if knight.equipped:
                    knight.equipped.cell = new_cell

                new_cell.items.sort(key=attrgetter('value'))
                if not knight.equipped:
                    knight.equipped = new_cell.items.pop()

            return knight

    def change_position(self, cell: Cell, direction):
        """
            This method updates the cell details of the knights, given directions.
            Returns the board in the new state i.e updated movements as at when called.
        """
         
        new_x = 0
        new_y = 0

        if direction == 'N':
            new_x = cell.x - 1
            new_y = cell.y
        elif direction == 'E':
            new_x = cell.x 
            new_y = cell.y + 1
        elif direction == 'W':
            new_x = cell.x
            new_y = cell.y - 1
        elif direction == 'S':
            new_x = cell.x + 1
            new_y = cell.y

        if (new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7):
            raise Exception("Knight Drowns")
        
        return self.board[new_x][new_y]


    def attack(self, attacker, defender):
        """ 
            Simulates the attack following the instructions given
            Returns [winner, loser]
        """
        total_attack = attacker.base_attack_score + 0.5
        total_defense = defender.base_defense_score

        if attacker.equipped:
            total_attack += attacker.equipped.attack_score
        
        if defender.equipped:
            total_defense += defender.equipped.defense_score

        if total_attack > total_defense:
            return (attacker, defender)
        else:
            return (defender, attacker)

    def kill_knight(self, knight, status):
        """
            This method essentially nullifies a dead knight and set's the status to either DEAD or DROWNED, depending on the status index provided.
        """

        item = knight.equipped
        position = knight.cell

        knight.status = Board.STATUS[status]
        knight.cell = None #None as there is no null in Python
        knight.equipped = None
        knight.base_attack_score = 0
        knight.base_defense_score = 0

        return (item, position)