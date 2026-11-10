import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(6, multiply(2, 3))
        self.assertEqual(-6, multiply(-2, 3))
        self.assertEqual(0, multiply(0, 5))


    def test_divide(self): # 3 assertions
        self.assertEqual(2, divide(4, 2))
        self.assertEqual(-4, divide(-4, 2))
        self.assertEqual(0, divide(0, 5))


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertIsNone(logarithm(0, 5))
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypothenuse(3, 4))
        self.assertEqual(13, hypothenuse(5, 12))
        self.assertEqual(7, hypothenuse(0, 7))

    def test_sqrt(self): # 3 assertions
        self.assertIsNone(square_root(-1))
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        self.assertEqual(3, square_root(9))
        self.assertEqual(1.5, square_root(2.25))
        self.assertEqual(0, square_root(0))
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()