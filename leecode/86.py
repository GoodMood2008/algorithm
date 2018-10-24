#!/user/bin/python
#-*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
class Solution:
    def print(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    def convertArrayToList(self, array):
        if len(array) == 0:
            return None
        head = result = ListNode(array[0])
        for i in array[1:]:
            result.next = ListNode(i)
            result = result.next
        return head

    def convertListToArray(self, head):
        if head == None:
            return []
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        sentinel1 = ListNode(-1)
        sentinel2 = ListNode(-1)
        cur1 = sentinel1
        cur2 = sentinel2
        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur2.next = None
        cur1.next = sentinel2.next
        return sentinel1.next

                




# T(n) = Nlgk
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 4, 3, 2, 5, 2]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.partition(head, 3)) == [1, 2, 2, 4, 3, 5])

if __name__ == "__main__" : unittest.main()
