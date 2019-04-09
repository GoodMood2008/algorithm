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
        print(head)
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
            print("%d "%(cur.val))
            cur = cur.next  
        print()  

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        sentinel = ListNode(None)
        sentinel.next, prev, cur = head, sentinel, head
        while cur:
            val = cur.val
            while cur.next:
                if cur.next.val == val:
                    cur = cur.next
                else:
                    break
            prev.next, prev, cur = cur, cur, cur.next
        return sentinel.next


#Given a sorted linked list, delete all duplicates such that each element appear only once.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 1, 2]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.deleteDuplicates(head)) == [1, 2])
        array = [1, 1, 2, 3, 3]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.deleteDuplicates(head)) == [1, 2, 3])        

if __name__ == "__main__" : unittest.main()
