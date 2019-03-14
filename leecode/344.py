#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'int':
        major, counts, size = 0, 0, len(nums)
        for num in nums:
            if not counts:
                major = num
                counts = 1
            else:
                counts += 1 if num == major else -1
        return major                
        


#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.majorityElement([3,2,3]) == 3)
        self.assertTrue(solution.majorityElement([2,2,1,1,1,2,2]) == 2)
        self.assertTrue(solution.majorityElement([3,3,4]) == 3)

if __name__ == "__main__" : unittest.main()
