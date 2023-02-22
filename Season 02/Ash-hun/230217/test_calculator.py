import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1,2),3)

    def test_sub(self):
        self.assertEqual(calculator.sub(1,2),-1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1,2),2)

    def test_divide(self):
        self.assertEqual(calculator.divide(1,2),0.5)

if __name__=="__main__":
    unittest.main()

