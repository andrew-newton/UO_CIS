"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_empty(self):
        self.assertEqual(max_run([ ]), [ ])

    def test02(self):
        self.assertEqual(max_run([0, 1, 1, 2, 2, 2, 1, 1, 3]), [2, 2, 2])

    def test03(self):
        a = max_run([1, 1, 2, 2, 1])
        b = max_run([2, 2, 2])
        self.assertEqual(b, [2, 2, 2])



if __name__ == "__main__":
    unittest.main()

