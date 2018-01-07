import unittest
import sys
sys.path.append('../')
from main import Main

class TestMain(unittest.TestCase):
    def test_sum(self):
        temp = Main()
        expected = 3
        actual = temp.sum(1, 2)
        self.assertEqual(expected, actual)

if __name__== '__main__':
    unittest.main()
