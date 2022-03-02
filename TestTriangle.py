# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right --------------------------------------------------------------------------------

    # Standard / smallest valid triangle
    def testRightTriangle01(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    # Flipped order
    def testRightTriangle02(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    # Largest valid triangle
    def testRightTriangle03(self):
        self.assertEqual(classify_triangle(28, 195, 197), 'Right',
                         '28, 195, 197 is a Right triangle')

    # Equilateral --------------------------------------------------------------------------

    # Smallest valid triangle

    def testEquilateralTriangle01(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    # Largest valid triangle
    def testEquilateralTriangle02(self):
        self.assertEqual(classify_triangle(200, 200, 200),
                         'Equilateral', '200,200,200 should be equilateral')

    # Isosceles ------------------------------------------------------------------------------

    # Largest valid triangle
    def testIsoscelesTriangle01(self):
        self.assertEqual(classify_triangle(199, 200, 200), 'Isosceles',
                         '199, 200, 200 is an Isosceles')

    # Smallest valid triangle
    def testIsoscelesTriangle02(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles',
                         '1, 2, 2 is an Isosceles')

    # Flipped Order
    def testIsoscelesTriangle03(self):
        self.assertEqual(classify_triangle(200, 200, 1), 'Isosceles',
                         '200, 200, 1 is an Isosceles')
                        
    # Flipped Order 2
    def testIsoscelesTriangle04(self):
        self.assertEqual(classify_triangle(200, 1, 200), 'Isosceles',
                         '200, 1, 200 is an Isosceles')

    # Scalene --------------------------------------------------------------------------------

    # Standard
    def testScaleneTriangle01(self):
        self.assertEqual(classify_triangle(7, 12, 15), 'Scalene',
                         '7, 12, 15 should be Scalene')

    # Flipped Order
    def testScaleneTriangle02(self):
        self.assertEqual(classify_triangle(15, 7, 12), 'Scalene',
                         '15, 7, 12 should be Scalene')

    # Smallest Valid Triangle
    def testScaleneTriangle03(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene',
                         '2, 3, 4 is a Scalene triangle')

    # InvalidInput ---------------------------------------------------------------------------

    # negative
    def testInvalidInput01(self):
        self.assertEqual(classify_triangle(-1, -1, -1),
                         'InvalidInput', '-1, -1, -1 is invalid')

    # non-int
    def testInvalidInput02(self):
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), 'InvalidInput',
                         '1, 1, sqrt(2) is invalid')

    # Zero
    def testInvalidInput03(self):
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput',
                         '0,0,0 is invalid')

    # non-int float
    def testInvalidInput04(self):
        self.assertEqual(classify_triangle(1.2, 1.2, 1.2), 'InvalidInput',
                         '1.2, 1.2, 1.2 is invalid')

    # # non-int string
    # def testInvalidInput05(self):
    #     self.assertEqual(classify_triangle("a", "a", "a"), 'InvalidInput',
    #                      '"a", "a", "a" is invalid')
                    
    # Too large
    def testInvalidInput06(self):
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput',
                         '201, 201, 201 is invalid')

    # Not A Triangle ---------------------------------------------------------------------------

    # Side lengths invalid
    def testNotATriangleInput01(self):
        self.assertEqual(classify_triangle(10, 15, 30),
                         'NotATriangle', '10,15,30 is a Not a Triangle')

    # Flipped Order
    def testNotATriangleInput02(self):
        self.assertEqual(classify_triangle(30, 15, 10),
                         'NotATriangle', '30, 15, 10 is a Not a Triangle')
                        
    # Flipped Order 2
    def testNotATriangleInput03(self):
        self.assertEqual(classify_triangle(10, 30, 15),
                         'NotATriangle', '10, 30, 15 is a Not a Triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
