#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    # BF T(n) = O(2^n)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.maxLen = 0
        self.dfs(nums, [], 0)
        return self.maxLen

    def dfs(self, nums, value, pos):
        if pos == len(nums) - 1:
            if self.increasingSeq(value):
                self.maxLen = max(self.maxLen, len(value))
            return
        self.dfs(nums, value, pos + 1)
        # optimize
        if (value and value[-1] <= nums[pos]) or not value:
            self.dfs(nums, value + [nums[pos]], pos + 1)

    def increasingSeq(self, value):
        if not value:
            return True
        cur = value[0]
        for num in value[1:]:
            if cur > num:
                return False
            cur = num
        return True

    # DP
    # T(n) = O(n^2)
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            j = i - 1
            if j < 0:
                dp[i] = 1
            else:
                dp[i] = self.maxDp(dp, j, nums, i) + 1
        return max(dp)

    # get the max dp that num is less than nums[i]
    def maxDp(self, dp, j, nums, i):
        samllerDp = []
        for k in range(j + 1):
            if nums[i] > nums[k]:
                samllerDp.append(dp[k])
        if samllerDp:
            return max(samllerDp)
        else:
            return 0

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


#Given an unsorted array of integers, find the length of longest increasing subsequence.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        self.assertTrue(solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4)
        self.assertTrue(solution.lengthOfLIS1([10,9,2,5,3,7,101,18]) == 4)

if __name__ == "__main__" : unittest.main()