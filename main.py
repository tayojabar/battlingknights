from board import Board 
from knight import Knight
from item import Item

from util import Utils

from pprint import pprint

# arena = Board()
# pprint (arena.board)

class BattlingKnights:

    def default_board(self): 
        """
            Setup the board in the formation provided in the instructions
        """

        self.battle_field = Board()
        board = (self.battle_field.board)

        self.R = Knight('R', 'red', board[0][0])
        self.Y = Knight('Y', 'yellow', board[0][7])
        self.G = Knight('G', 'green', board[7][7])
        self.B = Knight('B', 'blue', board[7][0])

        self.axe = Item('Axe', 4, board[2][2], 2, 0)
        self.dagger = Item('Dagger', 2, board[2][5], 1, 0)
        self.helmet = Item('Helmet', 1, board[5][5], 0, 1)
        self.magicstaff = Item('MagicStaff', 3, board[5][2], 1, 1)

        board[0][0].knight = self.R
        board[0][7].knight = self.Y
        board[7][7].knight = self.G
        board[7][0].knight = self.B

        board[2][2].items.append(self.axe)
        board[2][5].items.append(self.dagger)
        board[5][2].items.append(self.magicstaff)
        board[5][5].items.append(self.helmet)

        starter = (
                    self.battle_field.board,
                    self.R,
                    self.Y,
                    self.B,
                    self.G,
                    self.axe,
                    self.dagger,
                    self.helmet,
                    self.magicstaff
                )
        return starter

    def play_game(self):

        """
            Read the file using the utility function and move the knights according to moves in the file.
            print statements for visualizing the steps
        """

        moves = Utils.read_moves()
        count = 0
        for (id, direction) in moves:
            print("Move ", count, "=>", id, ":", direction, "\n")
            knight = getattr(self, id)
            self.battle_field.move(knight, direction)
            count = count + 1

if __name__ == '__main__':
    """ Essentially a main method """

    bk = BattlingKnights()
    (
        battle_field,
        R, Y, G, B,
        Axe, 
        Dagger, 
        Helmet, 
        MagicStaff
    ) = bk.default_board()

    bk.play_game()
    Utils.write_to_file(Utils.save_game([R, Y, G, B], [Axe, Dagger, Helmet, MagicStaff]))