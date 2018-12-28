#!/user/bin/python
#-*- coding:utf-8 -*-
import sys

#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete at most two transactions.
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]

        maxint = sys.maxsize
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = -maxint, -maxint
        profit[0][2][0], profit[0][2][1] = -maxint, -maxint

        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0] - prices[i])

            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0] - prices[i])

            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1] + prices[i])

        end = len(prices) - 1

        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])
            



import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.maxProfit([3,3,5,0,0,3,1,4]) == 6)
        self.assertTrue(solution.maxProfit([1,2,3,4,5]) == 4)
        self.assertTrue(solution.maxProfit([7,6,4,3,1]) == 0)


if __name__ == "__main__" : unittest.main()
