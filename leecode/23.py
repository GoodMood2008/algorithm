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

    def mergeTwoList(self, list1, list2):
        cur1 = list1
        cur2 = list2
        sentinel = ListNode(-1)
        cur = sentinel
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        return sentinel.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        elif len(lists) == 1:
            return lists[0]
        middle = int(len(lists)/2)
        left = self.mergeKLists(lists[:middle])
        left = mergeKLists(lists[middle:])
        return self.mergeTwoList(left, right)



# T(n) = Nlgk
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array1 = [1, 4, 5]
        array2 = [1, 3, 4]
        array3 = [2, 6]
        head1 = solution.convertArrayToList(array1)
        head2 = solution.convertArrayToList(array2)
        head3 = solution.convertArrayToList(array3)
        self.assertTrue(solution.convertListToArray(solution.mergeKLists([head1, head2, head3])) == [1, 1, 2, 3, 4, 4, 5, 6])

if __name__ == "__main__" : unittest.main()
