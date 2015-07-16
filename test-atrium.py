import unittest
from Atrium import Atrium
from Bishop import Bishop

class TestAtrium(unittest.TestCase):

    def test_centre(self):
        peter = Bishop(76);
        self.assertEqual(peter.coords(), [8 ,4])

    def test_top(self):
        peter = Bishop(8);
        self.assertEqual(peter.type(), 'T')

    def test_top(self):
        peter = Bishop(151);
        self.assertEqual(peter.type(), 'B')

    def test_left(self):
        peter = Bishop(102);
        self.assertEqual(peter.type(), 'L')

    def test_middle(self):
        peter = Bishop(76);
        self.assertEqual(peter.type(), 'M')

    def test_corners(self):
        peter = Bishop(0);
        self.assertEqual(peter.type(), 'a')
        peter = Bishop(16);
        self.assertEqual(peter.type(), 'b')
        peter = Bishop(136);
        self.assertEqual(peter.type(), 'c')
        peter = Bishop(152);
        self.assertEqual(peter.type(), 'd')

    def test_print_start(self):
        peter = Bishop(76);
        atrium = Atrium(peter);
        emptyAtrium = open('blank_atrium.txt', 'r').read()
        self.assertEqual(str(atrium), emptyAtrium)

    def test_print_single_move(self):
        peter = Bishop(76);
        atrium = Atrium(peter);
        atrium.move(0)
        dottyAtrium = open('atrium_single_move.txt', 'r').read()
        self.assertEqual(str(atrium), dottyAtrium)

    def test_print_repeated_move(self):
        peter = Bishop(76);
        atrium = Atrium(peter);
        atrium.move(0)
        atrium.move(3)
        atrium.move(0)
        atrium.move(3)
        atrium.move(0)
        atrium.move(3)
        dottyAtrium = open('atrium_multiple_move.txt', 'r').read()
        self.assertEqual(str(atrium), dottyAtrium)
