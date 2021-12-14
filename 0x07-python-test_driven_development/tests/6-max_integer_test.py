#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases to be evaluated.
    """

    def test_max_end(self):
        """Test max int of a list
        """
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lst), 5)

    def test_max_first(self):
        """Test max int of a list at the end
        """
        lst = [5, 4, 1, 3, 2]
        self.assertEqual(max_integer(lst), 5)

    def test_max_middle(self):
        """Test max int in the middle of a list
        """
        lst = [1, 4, 5, 2, 3]
        self.assertEqual(max_integer(lst), 5)

    def test_max_duplicate(self):
        """Test max int of duplicate values 
        """
        lst = [1, 4, 5, 2, 3, 5]
        self.assertEqual(max_integer(lst), 5)

    def test_max_one(self):
        """Test max int of  one element list
        """
        lst = [-1]
        self.assertEqual(max_integer(lst), -1)

    def test_max_negative(self):
        """Checks the max negative int of a list
        """
        lst = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(lst), -1)

    def test_float(self):
        """Checks the max float of a list
        """
        lst = [1.5, 2, 3.9, 4.56]
        self.assertEqual(max_integer(lst), 4.56)

    def test_string(self):
        """Checks max int(within the list a string)
        """
        lst = [1, 2, '3', 4]
        with self.assertRaises(TypeError):
            max_integer(lst)

    def test_empty_list(self):
        """Checks the case of an empty list
        """
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_void_arg(self):
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
