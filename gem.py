

# the matrix for the gem puzzle, and the
# blank moving operations.
# tw=45
#############################################

# TODO easy move, win

from random import choice


### Foundational Functions
def subGroup(lst, size):
    """Group the elements of lst into 
    sublists of size size.
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
        self.diff = self.diffMap()


### Movement. How do you move?
    def xchgBoard(self,
            yA, xA,
            yB, xB ):
        """Exchange positions of two pieces
        in the board.
        """
        # point A
        pA = self.board[yA][xA]
        pB = self.board[yB][xB]
        self.board[yA][xA] = pB
        self.board[yB][xB] = pA

    def move(self, yTo, xTo):
        """Exchange piece in position
        (yTo xTo) with blank.
        """
        if yTo < 0 or xTo < 0:
            raise IndexError

        self.xchgBoard(
                yTo, xTo,
                self.blank.y, self.blank.x )
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


### Move mapping. What message makes me move
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


### User movement. Where can they move

    def whereCanIGo(self):
        """In my current position, where can
        the blank move?

        Return a list of strings
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

    def doMove(self, whereTo):
        """Take a move key
        (up, down, left, right),
        execute a move function.
        """
        self.moveMap[whereTo]()

    def usrCross(self):
        """a string to tell them where they 
        can go.
        """
        crossRoad = ""
        for way in self.whereCanIGo():
            crossRoad += way+" "

        return crossRoad


### Difficulty. How hard can it get?

    def diffMap(self):
        return {
                0   :   0,
                1   :   10,
                2   :   50,
                3   :   100,
                }

    def rndMove(self):
        self.doMove(
                choice(
                    self.whereCanIGo() ) )

    def scramble(self, iterations):
        for i in range(iterations):
            self.rndMove()

    def howDifficult(self, howD):
        self.scramble(self.diff[howD])


### Printing. Show me the board.
    def pBoard(self):
        """Print the board, simply.
        """
        spaces = self.XLEN*"\t{}"
        for y in range(self.YLEN):
            print(spaces.format(
                    *self.board[y] ) )


### Validate. Did the right thing come in?

    def insist():
        """Decorator. Run fun until it does
        not return one of the exceptions.
        """
        def decorator(fun):
            def wrapper(*args, **kws):
                while True:
                    try:
                        return fun(*args, **kws)
                    # bad, hard code
                    except IndexError:
                        msg = "\tCan'g go\n"
                        print(msg)
                    except KeyError:
                        msg = "\tundefined\n"
                        print(msg)
                    except ValueError:
                        print("that is not a number")
            return wrapper
        return decorator


### User interaction cycle. Ask and do.
    
    @insist()
    def readAndRun(self):
        """Get user input.
        If they input an empty line, 
        return False.
        if good, move and return True.
        if bad, ask again.
        """
        moveTo = input(
                self.usrCross()
                +": " )
        if moveTo == '':
            return False
        self.doMove(moveTo)
        return True

    @insist()
    def doDifficulty(self):
        msg = "How hard do you want it? "
        for d, it in self.diff.items():
            msg += str(d)+" "

        dif = int(input(msg))
        self.howDifficult(dif)
        return dif

    def main(self):
        """Loop until false:
        print matrix,
        change matrix.
        """

        self.doDifficulty()

        again = True
        while again:
            self.pBoard()
            print("where to?")
            again = self.readAndRun()

###


ava = GemBoard(4, 4)


