import unittest
import LeapYr

class TestCase(unittest.TestCase):
    def test_not4(self):
        self.assertEqual(LeapYr.go(3),0)
        self.assertEqual(LeapYr.go(43),0)
        self.assertEqual(LeapYr.go(2021),0)
    def test_4not100(self):
        self.assertEqual(LeapYr.go(16),1)
        self.assertEqual(LeapYr.go(44),1)
        self.assertEqual(LeapYr.go(2020),1)

