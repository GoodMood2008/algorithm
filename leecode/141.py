#!/user/bin/python
#-*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            print(fast.val)
            print(slow.val)
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        print(fast.val)
        print(slow.val)
        return False




#Given a linked list, determine if it has a cycle in it.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        head = ListNode(5)
        cur = head
        cur.next = ListNode(4)
        cur = cur.next
        cur.next = ListNode(3)
        cur = cur.next
        cur.next = ListNode(2)
        cur = cur.next
        cur.next = ListNode(1)
        cur = cur.next

        cur.next = head.next.next
                        
        self.assertTrue(solution.hasCycle(head))

if __name__ == "__main__" : unittest.main()
