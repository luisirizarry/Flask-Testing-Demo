from algorithms import reverse_str, is_palindrome, factorial
from unittest import TestCase

class AlgorithmsTestCase(TestCase):
    def test_revers(self):
        self.assertEqual(reverse_str('hello'), 'olleh')
        self.assertEqual(reverse_str('Apple'), 'elppA')

    def test_is_palinddrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('RACEcar'))
        self.assertTrue(is_palindrome('KAYAK'))
        self.assertTrue(is_palindrome('kayak'))
        self.assertTrue(is_palindrome('Taco'))
        self.assertTrue(is_palindrome('Tacocat'))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(2), 3)
        self.assertRaises(ValueError, factorial, .2)
        self.assertRaises(ValueError, factorial, -.2)
        self.assertRaises(ValueError, factorial, -2)