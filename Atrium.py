
class Atrium(object):

    def __init__(self, bishop, key_type, hashtype):

        self.bishop = bishop
        self.counts = [0] * 153
        self.counts[76] = 15
        self.key_type = key_type
        self.hashtype = hashtype


    def move(self, step):
        self.bishop.move(step)
        if self.counts[self.bishop.location()] < 15:
            self.counts[self.bishop.location()] += 1

    def finalise(self, step):
        self.bishop.move(step)
        self.counts[self.bishop.location()] = 16

    def coin(self, count):
            return {
            0: ' ',
            1: '.',
            2: 'o',
            3: '+',
            4: '=',
            5: '*',
            6: 'B',
            7: 'O',
            8: 'X',
            9: '@',
            10: '%',
            11: '&',
            12: '#',
            13: '/',
            14: '^',
            15: 'S',
            16: 'E',
            }.get(count)

    def __str__(self):
        keytype = '['+self.key_type+']-'
        output = '+'+keytype.center(17, '-')+'+\n'
        for idx, val in enumerate(self.counts):
            coin = self.coin(val)
            if idx % 17 == 0:
                output += '|'
            output += coin
            if (idx+1) % 17 == 0:
                output += '|\n'
        hashtype = '['+self.hashtype+']'
        output += '+'+hashtype.center(17, '-')+'+'
        return output