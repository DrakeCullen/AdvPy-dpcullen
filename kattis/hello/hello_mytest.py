#!/usr/bin/env python3
import unittest
from hello import hello

class HelloTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello World!", "Not Hello World!")

if __name__ == "__main__":
    unittest.main(verbosity=2)
