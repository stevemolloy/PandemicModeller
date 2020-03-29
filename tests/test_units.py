import unittest

from Pyndemic.units import HouseHold

class TestHouseHold(unittest.TestCase):
    def test_basics(self):
        h = HouseHold(2, 2, 0)
        self.assertEqual(h.members.kids, 2)
        self.assertEqual(h.members.adults, 2)
        self.assertEqual(h.members.retirees, 0)

if __name__ == "__main__":
    unittest.main()

