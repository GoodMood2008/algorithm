#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPri, maxPro = prices[0], 0
        for p in prices[1:]:
            if p < minPri:
                minPri = p
            else:
                maxPro = max(maxPro, p - minPri)
        return maxPro

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        profit = [[0 for i in range(3)] for i in range(len(prices))]

        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            res = max(res, max(profit[i]))

        return res

import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        input = [7,1,5,3,6,4]
        self.assertTrue(solution.maxProfit(input) == 5)
        self.assertTrue(solution.maxProfit1(input) == 5)

if __name__ == "__main__" : unittest.main()