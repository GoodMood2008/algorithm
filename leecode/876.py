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

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        sentinal = ListNode(0)
        first, second, sentinal.next = sentinal, sentinal, head

        while second.next and second.next.next:
            first, second = first.next, second.next.next

        return first .next 

    def middleNode1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1,2,3,4,5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.middleNode(head).val == 3)
        self.assertTrue(solution.middleNode1(head).val == 3)

        array = [1,2,3,4,5,6]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.middleNode(head).val == 4)
        self.assertTrue(solution.middleNode1(head).val == 4)

if __name__ == "__main__" : unittest.main()