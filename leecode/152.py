#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]

        dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
            dp[x][1] = min(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
            res = max(res, dp[x][0])

        return res

    def maxProduct1(self, nums):
        if not nums: return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]
        maxr, minr, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            maxr, minr = max(maxr * nums[i], minr * nums[i], nums[i]), \
                        min(maxr * nums[i], minr * nums[i], nums[i])
            res = max(res, maxr)

        return res


#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
#which has the largest product.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.maxProduct([2,3,-2,4]) == 6)
        self.assertTrue(solution.maxProduct([-2,0,-1]) == 0)
        self.assertTrue(solution.maxProduct1([2,3,-2,4]) == 6)
        self.assertTrue(solution.maxProduct1([-2,0,-1]) == 0)

if __name__ == "__main__" : unittest.main()
