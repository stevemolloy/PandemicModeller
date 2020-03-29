import unittest

from Pyndemic.units import HouseHold

class TestHouseHold(unittest.TestCase):
    def test_basics(self):
        h = HouseHold(2, 2, 0)
        self.assertEqual(h.members.kids, 2)
        self.assertEqual(h.members.adults, 2)
        self.assertEqual(h.members.retirees, 0)

        self.assertEqual(h.S.kids, 2)
        self.assertEqual(h.S.adults, 2)
        self.assertEqual(h.S.retirees, 0)

        self.assertEqual(h.E.kids, 0)
        self.assertEqual(h.E.adults, 0)
        self.assertEqual(h.E.retirees, 0)

        self.assertEqual(h.I.kids, 0)
        self.assertEqual(h.I.adults, 0)
        self.assertEqual(h.I.retirees, 0)

        self.assertEqual(h.R.kids, 0)
        self.assertEqual(h.R.adults, 0)
        self.assertEqual(h.R.retirees, 0)

    def test_infecting(self):
        h = HouseHold(2, 2, 0)
        h.infect(1, 0, 0)
        self.assertEqual(h.E.kids, 1)
        self.assertEqual(h.E.adults, 0)
        self.assertEqual(h.E.retirees, 0)

        self.assertEqual(h.I.kids, 0)
        self.assertEqual(h.I.adults, 0)
        self.assertEqual(h.I.retirees, 0)

        self.assertEqual(h.R.kids, 0)
        self.assertEqual(h.R.adults, 0)
        self.assertEqual(h.R.retirees, 0)

if __name__ == "__main__":
    unittest.main()

