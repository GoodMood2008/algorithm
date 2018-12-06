#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    # T(n) = O(n)
    # S(n) = O(1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2: return n

        first,second = 1, 2
        stair = 0
        for i in range(3, n + 1):
            stair = first + second
            first, second = second, stair

        return stair




#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        self.assertTrue(solution.climbStairs(3) == 3)
        self.assertTrue(solution.climbStairs(4) == 5)

if __name__ == "__main__" : unittest.main()