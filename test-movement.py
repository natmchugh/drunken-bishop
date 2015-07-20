import unittest
from Bishop import Bishop


class TestMovement(unittest.TestCase):

  def test_move_up_left(self):
      peter = Bishop(76)
      peter.move(0)
      self.assertEqual(peter.location(), 58)

  def test_move_down_left(self):
      peter = Bishop(76)
      peter.move(2)
      self.assertEqual(peter.location(), 92)

  def test_move_down_right(self):
      peter = Bishop(76)
      peter.move(3)
      self.assertEqual(peter.location(), 94)

  def test_multiple_movments(self):
      peter = Bishop(76)
      peter.move(0)
      peter.move(1)
      peter.move(3)
      peter.move(2)
      self.assertEqual(peter.location(), 76)

  def test_hits_wall(self):
      peter = Bishop(84);
      peter.move(3)
      self.assertEqual(peter.location(), 101)

  def test_hits_left(self):
      peter = Bishop(85);
      peter.move(2)
      self.assertEqual(peter.location(), 102)

  def test_hits_ceiling(self):
      peter = Bishop(8);
      peter.move(1)
      self.assertEqual(peter.location(), 9)

  def test_hits_floor(self):
      peter = Bishop(144);
      peter.move(3)
      self.assertEqual(peter.location(), 145)

  def test_hits_corner(self):
      peter = Bishop(152);
      peter.move(1)
      self.assertEqual(peter.location(), 135)


if __name__ == '__main__':
    unittest.main()