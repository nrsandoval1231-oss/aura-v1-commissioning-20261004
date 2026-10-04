import unittest

from greeting import greet


class GreetingTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greet("Ada"), "Hi, Ada.")


if __name__ == "__main__":
    unittest.main()
