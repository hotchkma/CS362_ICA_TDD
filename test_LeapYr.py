import unittest
import LeapYr

class TestCase(unittest.TestCase):
    def test_not4(self):
        self.assertEqual(LeapYr.go(3),0)
        self.assertEqual(LeapYr.go(43),0)
        self.assertEqual(LeapYr.go(2021),0)
