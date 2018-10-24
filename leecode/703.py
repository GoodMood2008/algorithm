#!/user/bin/python
#-*- coding:utf-8 -*-
import queue

class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.priQueue = queue.PriorityQueue(k)
        self.kth = None
        for i in nums:
            if self.priQueue.full():
                smallest = self.priQueue.get()
                self.priQueue.put(i if i > smallest else smallest)
            else:
                self.priQueue.put(i)
        if not self.priQueue.empty():
            self.kth = self.priQueue.get()
            self.priQueue.put(self.kth)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.priQueue.full():
            if self.kth < val:
                self.priQueue.get()
                self.priQueue.put(val)  # reorder
                result = self.priQueue.get() # getsmallest
                self.priQueue.put(result)  # reput
                self.kth = result # update
                return result
            else:
                return self.kth
        else:
            self.priQueue.put(val)
            if self.priQueue.full():
                result = self.priQueue.get()
                self.kth = result
                self.priQueue.put(result)
                return result
            else:
                return None

import heapq
class KthLargest1:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.size = k
        heapq.heapify(nums)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
#Given a linked list, determine if it has a cycle in it.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        nums = [4, 5, 8, 2]
        kthL = KthLargest1(3, nums)
        self.assertTrue(kthL.add(3) == 4)
        self.assertTrue(kthL.add(5) == 5)
        self.assertTrue(kthL.add(10) == 5)
        self.assertTrue(kthL.add(9) == 8)
        self.assertTrue(kthL.add(4) == 8)

if __name__ == "__main__" : unittest.main()
