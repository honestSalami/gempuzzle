

# the matrix for the gem puzzle, and the
# blank moving operations.

def subGroup(lst, size):
    outLst = []
    tmpLst = list()
    position = 0
    length = len(lst) - 1

    while position < length:
        for i in range(size):
            tmpLst.append(lst[position])
            position += 1   # weird
        outLst.append(tmpLst)
        tmpLst = list() # weird

    return outLst

class Piece():
    def __init__(self, yPos, xPos):
        self.y = yPos
        self.x = xPos

    def shift(self, yNew, xNew):
        self.y = yNew
        self.x = xNew

class GemBoard():
    # Axis is the index, starts from 0
    # Len is the length, starts from 1

    def __init__(self,yLen, xLen):
        last = yLen*xLen
        lst = range(1, last + 1)
        self.board = subGroup(lst, xLen)
        self.YLEN  = yLen
        self.XLEN  = xLen
        self.yAxis = yLen - 1
        self.xAxis = xLen - 1
        #the blank is in the last position
        self.blank = Piece(
                    self.yAxis,
                    self.xAxis )
        self.board\
                [self.yAxis]\
                [self.xAxis] = 0

    def move(self, yTo, xTo):
        tmp = self.board[yTo][xTo]
        self.board[yTo][xTo] = 0
        self.board\
                [self.blank.y]\
                [self.blank.x] = tmp
        self.blank.shift(yTo, xTo)

    def up(self):
        self.move(
                self.blank.y - 1,
                self.blank.x )

    def down(self):
        self.move(
                self.blank.y + 1,
                self.blank.x )

    def left(self):
        self.move(
                self.blank.y,
                self.blank.x - 1 )

    def right(self):
        self.move(
                self.blank.y,
                self.blank.x + 1 )

    def pBoard(self):
        spaces = self.XLEN*"\t{}"
        for y in range(self.YLEN):
            print(spaces.format(
                    *self.board[y] ) )
