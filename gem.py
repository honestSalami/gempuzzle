

# the matrix for the gem puzzle, and the
# blank moving operations.
# tw=45
#############################################

# TODO validate, easy move, win


### Foundational Functions
def subGroup(lst, size):
    """Group the elements of lst into sublists
    of size size.
    """
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


### Piece class. This is what the blank is
class Piece():
    def __init__(self, yPos, xPos):
        self.y = yPos
        self.x = xPos

    def shift(self, yNew, xNew):
        self.y = yNew
        self.x = xNew


### Board Class
class GemBoard():
    # Axis is the index, starts from 0
    # Len is the length, starts from 1


    def __init__(self,yLen, xLen):
        """Make the board,
        set the LENgth and the Axis,
        construct the blank,
        place the blank on the board.
        """
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
        self.moveMap = self.mapFunc()


### Movement
    def move(self, yTo, xTo):
        """Exchange piece in position
        (yTo xTo) with blank.
        """
        tmp = self.board[yTo][xTo]
        self.board[yTo][xTo] = 0
        self.board\
                [self.blank.y]\
                [self.blank.x] = tmp
        self.blank.shift(yTo, xTo)

    # these are all, kinda, nullary functions
    # they still take the self, but meh...
    def up(self):
        """Move blank up
        """
        self.move(
                self.blank.y - 1,
                self.blank.x )

    def down(self):
        """Move blank down
        """
        self.move(
                self.blank.y + 1,
                self.blank.x )

    def left(self):
        """Move blank left
        """
        self.move(
                self.blank.y,
                self.blank.x - 1 )

    def right(self):
        """Move blank right
        """
        self.move(
                self.blank.y,
                self.blank.x + 1 )
### Movement mapping
    def mapFunc(self):
        return {
                "up"    :   self.up,
                "down"  :   self.down,
                "left"  :   self.left,
                "right" :   self.right
                }

    def usrFunc(self):
        return {
                "k"     :   "up",
                "j"     :   "down",
                "h"     :   "left",
                "l"     :   "right"
                }

### User movement. Their movement

    # fun list
    def whereCanIGo(self):
        """In my current position, where can
        the blank move?

        Returns a list of functions.
        """
        whereIndeed = []
        if self.blank.y > 0:
            whereIndeed.append("up")
        if self.blank.y < self.yAxis:
            whereIndeed.append("down")

        if self.blank.x > 0:
            whereIndeed.append("left")
        if self.blank.x < self.xAxis:
            whereIndeed.append("right")

        return whereIndeed

    def usrCross(self):
        """a string to tell them where they 
        can go.
        """
        crossRoad = ""
        for way in self.whereCanIGo():
            crossRoad += way+" "

        return crossRoad

    def doMove(self, whereTo):
        """Take a move key,
        execute a move function.
        """
        self.moveMap[whereTo]()

### Printing
    def pBoard(self):
        """Print the board, simply.
        """
        spaces = self.XLEN*"\t{}"
        for y in range(self.YLEN):
            print(spaces.format(
                    *self.board[y] ) )

### User interaction cycle
    def step(self):
        """Print the board,
        get user input,
        if none, stop,
        if good, move.

        If they input an empty line, 
        return False.
        Else, return True
        """
        self.pBoard()
        print("where to?")
        moveTo = input(
                self.usrCross()
                +": " )
        if moveTo == '':
            return False
        self.doMove(moveTo)
        return True
    
    def main(self):
        """Loop until false.
        """
        again = True
        while again:
            again = self.step()


ava = GemBoard(4, 4)


