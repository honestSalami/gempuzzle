#!  /data/data/com.termux/files/usr/bin/python

d = list(chr(i+100) for i in range(17))

def main_frame():
    numbers = '|{}|{}|{}|{}|'
    separate = '+-----+-----+-----+-----+'
    def spPrint(*args):
        print(separate)
        print(numbers.format(*args))

    spPrint(d[1], d[2], d[3], d[4])
    spPrint(d[5], d[6], d[7], d[8])
    spPrint(d[9], d[10], d[11], d[12])
    spPrint(d[13], d[14], d[15], d[16])
    print(separate)

def change(target):
    blank = position
    for a, b in self.items.items():
        if b == self.format(str(target)):
            piece = a
            break
    self.items[blank], self.items[piece] = self.items[piece], self.items[blank]
    self.position = piece

# find and exchange. an exchange function 
# might be better than a one liner like that
# maybe I dont need to change EVERY function

