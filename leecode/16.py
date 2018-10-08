#/user/bin/python
#-*- coding:utf-8 -*-

# traverse through is the basic method,but T(n) = O(n^3)
# then use the method underline, the most important thing is to write the right program
# it is not very easy
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            raise Exception("error input")
        result = nums[0] + nums[1] + nums[2]
        smallest = abs(result - target)
        for i, v in enumerate(nums):
            first = i + 1
            last = len(nums) - 1
            while first < last:
                tempsum = v + nums[first] + nums[last]
                if abs(tempsum - target) < smallest:
                    smallest = abs(tempsum - target)
                    result = tempsum
                if tempsum == target:
                    return tempsum
                elif tempsum > target:
                    last -= 1
                else:
                    first += 1
        return result     








import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self):
        solution = Solution()
        self.assertTrue(solution.threeSumClosest([0,-4,1,-5], 0) == -3)
        self.assertTrue(solution.threeSumClosest([1,2,5,10,11], 12) == 13)

if __name__ == "__main__" : unittest.main()