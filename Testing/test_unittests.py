import myfunction
import unittest

class TestMultiply(unittest.TestCase):
    def test_with_positive(self):
        self.assertEqual(myfunction.multiply_with_loop(17,19),17*19)
        self.assertEqual(myfunction.multiply_with_loop(1,2),2)
    
    def test_with_one_zero(self):
        self.assertEqual(myfunction.multiply_with_loop(17,0),0)
        self.assertEqual(myfunction.multiply_with_loop(0,2),0)

if __name__ == '__main__':
    unittest.main()
        
        