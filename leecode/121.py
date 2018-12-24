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


import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        input = [7,1,5,3,6,4]
        self.assertTrue(solution.maxProfit(input) == 5)

if __name__ == "__main__" : unittest.main()