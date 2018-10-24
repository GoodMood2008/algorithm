#!/user/bin/python
#-*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        cur = head
        while cur:
            if cur in nodes:
                return cur
            nodes.add(cur)
            cur = cur.next
        return None



#Given a linked list, determine if it has a cycle in it.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        head = ListNode(5)
        cur = head
        cur.next = ListNode(4)
        cur = cur.next
        begin = cur.next = ListNode(3)
        cur = cur.next
        cur.next = ListNode(2)
        cur = cur.next
        cur.next = ListNode(1)
        cur = cur.next

        cur.next = head.next.next
                        
        self.assertTrue(solution.detectCycle(head) == head.next.next)

if __name__ == "__main__" : unittest.main()
