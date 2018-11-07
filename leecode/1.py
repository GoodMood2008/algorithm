#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    # T(n) = O(n^2)
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]
                if target == (first + second):
                    return [i, j]
        raise Exception("No two numbers add equals to target")
            
    # T(n) = O(n)
    def twoSum(self, nums, target):
        indice = 0
        aDict = dict()
        for num in nums:
            aDict[num] = []
        for num in nums:
            aDict[num].append(indice)
            indice += 1
        for key, indices in aDict.items():
            indicefirst = indices.pop(0)
            pair = target - key
            if pair in aDict and aDict[pair]:
                return [indicefirst, aDict[pair].pop(0)]
        return []



#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.twoSum([2, 7, 11, 15], 9) == [0, 1])
        self.assertTrue(solution.twoSum([3, 3], 6) == [0, 1])


if __name__ == "__main__" : unittest.main()
