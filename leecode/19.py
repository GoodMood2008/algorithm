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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(None)
        sentinel.next = head

        first = second = sentinel
        i = 0
        while None != first:
            first = first.next
            if i > n:
                second = second.next
            i += 1
        second.next = second.next.next
        return sentinel.next

    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        i = n
        while i > 0:
            first = first.next
            i -= 1
        # get n + 1 Node
        second = ListNode(None)
        second.next = head
        while first != None:
            first = first.next
            second = second.next    

        #release n Node
        if None == second.val:
            return head.next
        second.next = second.next.next
        return head

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [5, 4, 3, 2, 1]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.removeNthFromEnd(head, 2)) == [5, 4, 3, 1])

        array = [1]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.removeNthFromEnd(head, 1)) == [])

        array = [1, 2]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.removeNthFromEnd(head, 2)) == [2])

if __name__ == "__main__" : unittest.main()