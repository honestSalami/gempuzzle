''' Structural Game for 15 - Puzzle with different difficulty levels'''
from random import randint


class Puzzle:
    def __init__(self):
        self.items = {} # dict of pieces
        self.position = None # space position

    def main_frame(self):
        """Print the board

        From a dictionary, of the piece 
        positions, print a square board
        """

        d = self.items
        numbers = '|{}|{}|{}|{}|'
        border  = '+-----+-----+-----+-----+'
        def spPrint(*args):
            print(border)
            print(numbers.format(*args))

        spPrint(d[1], d[2], d[3], d[4])
        spPrint(d[5], d[6], d[7], d[8])
        spPrint(d[9], d[10], d[11], d[12])
        spPrint(d[13], d[14], d[15], d[16])
        print(border)

    def format(self, ch):
        """Pad the piece number with spaces.
        """
        ch = ch.strip()
        if len(ch) == 1:
            return '  ' + ch + '  '
        elif len(ch) == 2:
            return '  ' + ch + ' '
        elif len(ch) == 0:
            return '     '


    def change(self, to):
        """Exchange piece and blank position.

        Find piece's position, save it,
        exchange it with blank's position.
        """
        fro = self.position
        for a, b in self.items.items():
            if b == self.format(str(to)):
                to = a
                break
        self.items[fro], self.items[to] = self.items[to], self.items[fro]
        self.position = to


    def build_board(self, difficulty):
        # make an ordered board
        for i in range(1, 17):
            self.items[i] = self.format(str(i))
        # find piece 16, make it  blank
        tmp = 0
        for a, b in self.items.items():
            if b == '  16 ':
                self.items[a] = '     '
                tmp = a
                break
        # why you need to find piece 16?
        # they are in order, its in index 16
        self.position = tmp
        if difficulty == 0:
            diff = 10
        elif difficulty == 1:
            diff = 50
        else:
            diff = 100
        # the more times you do it,
        # the harder it becomes
        for _ in range(diff):
            lst = self.valid_moves()
            lst1 = []
            for j in lst:
                lst1.append(int(j.strip()))
            # exchange a random piece and 
            # blank?
            # but it should be thought as:
            # make a random move
            self.change(lst1[randint(0, len(lst1)-1)])


    def valid_moves(self):
        """ Given the blank's position,
        return all positions you can move to,
        as a tuple.
        """
        # up    : -4
        # down  : +4
        # left  : -1
        # right : +1
        pos = self.position
        # if in middle square
        if pos in [6, 7, 10, 11]:
            # a tuple of 4 piece?
            return self.items[pos - 4], self.items[pos - 1],\
                   self.items[pos + 1], self.items[pos + 4]
        elif pos in [5, 9]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos + 1]
        elif pos in [8, 12]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos - 1]
        elif pos in [2, 3]:
            return self.items[pos - 1], self.items[pos + 1], self.items[pos + 4]
        elif pos in [14, 15]:
            return self.items[pos - 1], self.items[pos + 1],\
                  self.items[pos - 4]
        elif pos == 1:
            return self.items[pos + 1], self.items[pos + 4]
        elif pos == 4:
            return self.items[pos - 1], self.items[pos + 4]
        elif pos == 13:
            return self.items[pos + 1], self.items[pos - 4]
        elif pos == 16:
            return self.items[pos - 1], self.items[pos - 4]


    def game_over(self):
        flag = False
        for a, b in self.items.items():
            if b == '     ':
                pass
            else:
                if a == int(b.strip()):
                    flag = True
                else:
                    flag = False
        return flag




g = Puzzle()
g.build_board(int(input('Enter the difficulty : 0 1 2\n2 '
                        '=> highest 0=> lowest\n')))
g.main_frame()
print('Enter 0 to exit')
while True:
    print('Hello user:\nTo change the position just enter the no. near it')
    lst = g.valid_moves()
    lst1 = []
    for i in lst:
        lst1.append(int(i.strip()))
        print(i.strip(), '\t', end='')
    print()
    x = int(input())
    if x == 0:
        break
    elif x not in lst1:
        print('Wrong move')
    else:
        g.change(x)
    g.main_frame()
    if g.game_over():
        print('You WON')
        break
