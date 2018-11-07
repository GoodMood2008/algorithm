# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self):
        head = tail = ListNode(1)
        tail.next = ListNode(2)
        tail = tail.next
        tail.next = ListNode(3)
        tail = tail.next
        
        solution = Solution()


if __name__ == "__main__" : unittest.main()