# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(fst, snd, thrd):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    bool1 = not(isinstance(fst, int) and isinstance(
        snd, int) and isinstance(thrd, int))

    bool2 = fst <= 0 or snd <= 0 or thrd <= 0

    bool3 = fst > 200 or snd > 200 or thrd > 200

    if bool1 or bool2 or bool3:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (fst >= (snd + thrd)) or (snd >= (fst + thrd)) or (thrd >= (fst + snd)):
        return 'NotATriangle'

    sides = [fst, snd, thrd]
    sides.sort()
    # now we know that we have a valid triangle
    if fst == snd and snd == thrd:
        return 'Equilateral'
    if ((sides[0] ** 2) + (sides[1] ** 2)) == (sides[2] ** 2):
        return 'Right'
    if (fst != snd) and (snd != thrd) and (fst != thrd):
        return 'Scalene'
    return 'Isosceles'
