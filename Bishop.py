import math

from Atrium import Atrium

class Bishop(object):
 
    def __init__(self, pos):
        self.pos = pos

    def coords(self):
        x = self.pos % 17
        y = int(math.floor(self.pos / 17));
        return [x, y]

    def type(self):
        [x, y] = self.coords();
        if y == 0:
            if x == 0:
              return 'a'
            if x == 16:
              return 'b'
            return 'T'
        if x == 0:
            if y == 8:
              return 'c'
            return 'L'
        if x == 16:
            if y == 8:
              return 'd'
            return 'R'
        if y == 8:
            return 'B'
        return 'M'


    def move(self, step):
        w = 0
        squareType = self.type()
        # quite literally corner cases
        if 'a' == squareType:
            w = {
                0: 18,
                1: 17,
                2: 1
            }.get(step, 0)
        if 'b' == squareType:
            w = {
                0: 17,
                1: 16,
                3: 1
            }.get(step, 0)
        if 'c' == squareType:
            w = {
                0: 1,
                2: -16,
                3: -17
            }.get(step, 0)
        if 'd' == squareType:
            w = {
                1: -1,
                2: -17,
                3: -18
            }.get(step, 0)
        if 'R' ==  squareType and step % 2 == 1:
            w = -1
        if 'T' == squareType and step < 2:
            w = 17
        if 'B' == squareType and step > 1:
            w = -17
        if 'L' == squareType and step % 2 == 0:
            w = 1
        d = {
            0: -18,
            1: -16,
            2: 16,
            3: 18,
        } [step]
        self.pos += d + w

    def location(self):
        return self.pos
