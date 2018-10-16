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
        return result

    # 注释掉的那句看不出来为何结果不正确，dis也看不出来
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            #pre, cur, cur.next = cur, cur.next, pre
            cur.next, pre, cur, = pre, cur, cur.next
        return pre

    def reverseList1(self, head):
        if head == None or head.next == None:
            return head
        cur = head
        l = reverseList1(self, head.next)
        l.next = cur
        return l

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.reverseList(head)) == [5, 4, 3, 2, 1])
        self.assertTrue(solution.convertListToArray(solution.reverseList1(head)) == [5, 4, 3, 2, 1])

#if __name__ == "__main__" : unittest.main()

#import dis
#dis.dis(Solution)