#!/user/bin/python
#-*- coding:utf-8 -*-

# Definition for a binary tree node.


#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again)
class Solution:
    #greedy alg: T(n) = O(n)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) == 0:
            return 0
        prev = prices[0]
        for p in prices[1:]:
            if p > prev:
                result += p - prev
            prev = p
        return result





import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.maxProfit([7,1,5,3,6,4]) == 7)
        self.assertTrue(solution.maxProfit([1,2,3,4,5]) == 4)
        self.assertTrue(solution.maxProfit([7,6,4,3,1]) == 0)


if __name__ == "__main__" : unittest.main()
