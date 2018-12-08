#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        print(r)
        while r * r - x > 1:
            r = (r + x / r) / 2
            print(r)
        print(r)
        return int(r)





#Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.mySqrt(4) == 2)
        self.assertTrue(solution.mySqrt(8) == 2)
        self.assertTrue(solution.mySqrt(25) == 5)
if __name__ == "__main__" : unittest.main()
