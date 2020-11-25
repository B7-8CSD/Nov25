"""
Determine the row index with minimum number of ones.
The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise. 
If two or more rows have same number of 1's than print the row with smallest index.

input:
size of matrix: 3 3
0 0 0 0 0 0 0 0 0
output:  -1

size of matrix: 4 4
0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1
output: 0
"""

import unittest

def min_row(m,n,l):
    if h >= l: 
        m = l + (h - l)//2
        if (m == 0 or a[m - 1] == 0) and a[] == 1: 
            return mid 
        elif a[m] == 0: 
            return first(a, (m + 1), h) 
        else: 
            return first(a, l, (m - 1)) 
    return -1
    """
    m,n define size of matrix 
    l list of m*n elements
    """

# DO NOT TOUCH THE BELOW CODE
class TestCommonWords(unittest.TestCase):

    def test_01(self):
        l=[0,0,0,0,0,0,0,0,0]
        output = -1
        self.assertEqual(min_row(3,3,l), output)

    def test_02(self):
        l=[0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1]
        output = 0
        self.assertEqual(min_row(4,4,l), output)

    def test_03(self):
        l=[0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0]
        output = 3
        self.assertEqual(min_row(4,4,l), output)

    def test_04(self):
        l=[0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0]
        output = 0
        self.assertEqual(min_row(5,5,l), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
