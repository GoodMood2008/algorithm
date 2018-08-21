#!/bin/bash/python
#-*-coding:utf-8 -*-

class Solution:
    def mean(self, a, *paras):
        result = a
        for i in paras:
            result += i
        return (int)(result / 2)

    def findKth(self, nums1, nums2, pos):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            return nums2[pos - 1]
        if pos == 1:
            return min(nums1[0], nums2[0])

        m = min(self.mean(pos), len(nums1))
        if (nums1[m - 1] < nums2[pos - m - 1]):
            return self.findKth(nums1[m:], nums2, pos - m)
        else:
            return self.findKth(nums1, nums2[(pos - m):], m)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 0:
            return (self.findKth(nums1, nums2, self.mean(len1, len2)) + 
                self.findKth(nums1, nums2, self.mean(len1, len2) + 1)) / 2
        else:
            return self.findKth(nums1, nums2, self.mean(len1, len2) + 1)


import unittest
class SolutionTestCase(unittest.TestCase):
    def testfindMedian(self):
        solution = Solution()
        self.assertEqual(solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(solution.findMedianSortedArrays([1], [2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(solution.findMedianSortedArrays([1, 2, 3, 4, 5], [6]), 3.5)
        self.assertEqual(solution.findMedianSortedArrays([1], [2, 3, 4, 5]), 3.0)
        self.assertEqual(solution.findMedianSortedArrays([1, 2, 3, 4], [5]), 3.0)  
        self.assertEqual(solution.findMedianSortedArrays([], [1]), 0.5)        

if __name__ == "__main__": unittest.main()


