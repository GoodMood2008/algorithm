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
        print(result)
        return result

    def printList(self, head):
        cur = head
        while cur:
            print("%d "%(cur.val))
            cur = cur.next  
        print()  

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None

        centinail = ListNode(-1)
        prev, cur, last= head, head, head
        count = 0
        while cur:
            if count == k:
                last.next = self.reverseKGroup(cur, k)
                return centinail.next
            else:
                if prev is not cur:
                    centinail.next, cur = cur, cur.next, 
                    centinail.next.next, prev = prev, centinail.next
                else:
                    centinail.next, cur = prev, cur.next
                count += 1
        last.next = None
        return centinail.next

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        if not head: return None

        cur, count = head, 0
        while cur != None and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup1(cur, k)
            count -= 1
            while count:
                count -= 1
                temp = head.next
                head.next = cur
                cur.next = head
                head = temp
            head = cur
        return head





#Given this linked list: 1->2->3->4->5
#For k = 2, you should return: 2->1->4->3->5
#For k = 3, you should return: 3->2->1->4->5
#Only constant extra memory is allowed.
#You may not alter the values in the list's nodes, only nodes itself may be changed.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.reverseKGroup(head, 2)) == [2, 1, 4, 3, 5])
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.reverseKGroup(head, 3)) == [3, 2, 1, 5, 4])        
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.reverseKGroup1(head, 2)) == [2, 1, 4, 3, 5])
        array = [1, 2, 3, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.reverseKGroup1(head, 3)) == [3, 2, 1, 5, 4])


if __name__ == "__main__" : unittest.main()
