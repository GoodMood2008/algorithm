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

    def printList(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return None
        else:
            first, second = (l1, l2) if l1.val < l2.val else (l2, l1)
            first.next = self.mergeTwoLists(first.next, second)
            return first

    def mergeTwoListsIter(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentNail = ListNode(0)
        cur, first, second = sentNail, l1, l2
        while first and second:
            if first.val < second.val:
                cur.next = first
                first = first.next
                cur = cur.next
            else:
                cur.next = second
                second = second.next
                cur = cur.next
        cur.next = second if not first else first
        return sentNail.next







#Merge two sorted linked lists and return it as a new list. 
#The new list should be made by splicing together the nodes of the first two lists.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        first = solution.convertArrayToList([1, 2, 4])
        second = solution.convertArrayToList([1, 3, 4])
        self.assertTrue(solution.convertListToArray(solution.mergeTwoLists(first, second)) == [1, 1, 2, 3, 4, 4])
        first = solution.convertArrayToList([1, 2, 4])
        second = solution.convertArrayToList([1, 3, 4])
        self.assertTrue(solution.convertListToArray(solution.mergeTwoListsIter(first, second)) == [1, 1, 2, 3, 4, 4])

        first1 = solution.convertArrayToList([5])
        second1 = solution.convertArrayToList([1, 2, 4])
        self.assertTrue(solution.convertListToArray(solution.mergeTwoLists(first1, second1)) == [1, 2, 4, 5])
        first1 = solution.convertArrayToList([5])
        second1 = solution.convertArrayToList([1, 2, 4])
        self.assertTrue(solution.convertListToArray(solution.mergeTwoListsIter(first1, second1)) == [1, 2, 4, 5])

if __name__ == "__main__" : unittest.main()