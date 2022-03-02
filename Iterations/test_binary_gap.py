import unittest
from Iterations.binary_gap import max_binary_gap

class TestBinaryGap(unittest.TestCase):
    def test_1041_give_5(self):
        self.assertEqual(max_binary_gap(1041), 5)
        
    def test_32_give_0(self):
        self.assertEqual(max_binary_gap(32), 0)
        
    def test_9_give_2(self):
        self.assertEqual(max_binary_gap(9), 2)
        
    def test_529_give_4(self):
        self.assertEqual(max_binary_gap(529), 4)
        
    def test_20_give_1(self):
        self.assertEqual(max_binary_gap(20), 1)
        
    def test_15_give_0(self):
        self.assertEqual(max_binary_gap(15), 0)