#!/user/bin/python
#-*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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
        print(result)
        return result

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        centinail = ListNode(-1)
        centinail.next = head
        prev = centinail
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            a.next, b.next, prev.next = b.next, a, b
            prev = prev.next.next
        return centinail.next




#Given 1->2->3->4, you should return the list as 2->1->4->3.
#Your algorithm should use only constant extra space.
#You may not modify the values in the list's nodes, only nodes itself may be changed.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.swapPairs(head)) == [2, 1, 4, 3, 5])

if __name__ == "__main__" : unittest.main()
