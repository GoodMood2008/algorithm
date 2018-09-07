#/user/bin/python
#-*- coding:utf-8 -*-
import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = 1 if x > 0 else -1
        result = 0
        x *= symbol
        while x != 0 : 
           i = x % 10
           result = 10 * result + i
           x = (int)(x / 10)
        result *= symbol
        return 0 if (result > sys.maxsize or result < ~sys.maxsize) else result

import unittest
class SolutionTestCase(unittest.TestCase):
    def testReverse(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(1534236469), 0)

if __name__ == "__main__": unittest.main()
