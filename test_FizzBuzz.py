import unittest
import FizzBuzz

class TestCase(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(FizzBuzz.convert(3),"Fizz")
        self.assertEqual(FizzBuzz.convert(9),"Fizz")
        self.assertEqual(FizzBuzz.convert(81),"Fizz")
    def test_buzz(self):
        self.assertEqual(FizzBuzz.convert(5),"Buzz")
        self.assertEqual(FizzBuzz.convert(20),"Buzz")
        self.assertEqual(FizzBuzz.convert(65),"Buzz")
    def test_fizz_buzz(self):
        self.assertEqual(FizzBuzz.convert(15),"FizzBuzz")
        self.assertEqual(FizzBuzz.convert(45),"FizzBuzz")
        self.assertEqual(FizzBuzz.convert(90),"FizzBuzz")
        
