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
    def test_basic(self):
        self.assertEqual(FizzBuzz.convert(4),4)
        self.assertEqual(FizzBuzz.convert(7),7)
        self.assertEqual(FizzBuzz.convert(23),23)
    def test_prog(self):
        self.assertEqual(FizzBuzz.run(10),"1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz")
        self.assertEqual(FizzBuzz.run(3),"1 2 Fizz")
