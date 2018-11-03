#!/user/bin/python
#-*- coding:utf-8 -*-
import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        elif k == 1:
            return nums

        size = 0
        maxsize = len(nums)
        dq = collections.deque()

        result = []
        slideMax = nums[0]
        dq.append(slideMax)
        windowSize = 1
        for num in nums[1:]:
            if num >= slideMax:
                dq.clear()
                slideMax = num
                dq.append(num)
                windowSize = 1
            else:
                if windowSize < k:
                    dq.append(num)
                    windowSize += 1
                else:
                    dq.popleft()
                    dq.append(num)
                    slideMax = max(dq)
                    while True:
                        temp = dq.popleft()
                        windowSize -= 1
                        if temp == slideMax:
                            dq.appendleft(temp)
                            windowSize += 1
                            break
            size += 1
            if size >= k - 1 :
                result.append(slideMax)
        return result






#Given an array nums, there is a sliding window of size k which is 
#moving from the very left of the array to the very right. 
#You can only see the k numbers in the window. 
#Each time the sliding window moves right by one position. Return the max sliding window
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
        self.assertTrue(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 0) == [])
if __name__ == "__main__" : unittest.main()
