#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x, n = 1/x, -n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        print(result)
        return result

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, int(n/2))

import math
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(math.isclose(solution.myPow(2.00000, 10), 1024.00000))
        self.assertTrue(math.isclose(solution.myPow(2.10000, 3), 9.26100))
        self.assertTrue(math.isclose(solution.myPow(2.00000, -2), 0.25000))
        self.assertTrue(math.isclose(solution.myPow1(2.00000, 10), 1024.00000))
        self.assertTrue(math.isclose(solution.myPow1(2.10000, 3), 9.26100))
        self.assertTrue(math.isclose(solution.myPow1(2.00000, -2), 0.25000))      

if __name__ == "__main__" : unittest.main()

