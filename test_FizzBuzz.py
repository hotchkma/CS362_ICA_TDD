import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(FizzBuzz.convert(3),"Fizz")
        self.assertEqual(FizzBuzz.convert(9),"Fizz")
        self.assertEqual(FizzBuzz.convert(81),"Fizz")

