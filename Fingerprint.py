from Atrium import Atrium
from Bishop import Bishop

class Fingerprint(object):

    def __init__(self, hash):
        bishop = Bishop(76)
        self.atrium = Atrium(bishop)
        moves = self.hash_to_moves(hash)
        lastmove = moves.pop()
        print len(moves)
        for move in moves:
            self.atrium.move(move)
        self.atrium.finalise(lastmove)


    def __str__(self):
        return str(self.atrium)

    def hash_to_moves(self, hash):
        moves =[]
        for word in hash:
            for pair in (3, 2, 1, 0):
                shift = pair*8
                byte = (word & (255 << shift)) >> shift
                for step in range(0, 8, 2):
                  mask = 3 << step
                  move = (byte & mask) >> step
                  moves.append(move)
        return moves