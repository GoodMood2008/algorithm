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

    def printList(self, head):
        cur = head
        print('[', end='')
        while cur:
            print('%d '%cur.val, end='')
            cur = cur.next  
        print(']')  

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        cur = head
        count = 0
        while cur != None and count != k:
            cur = cur.next
            count += 1
        if count == k:
            newCur = self.reverseKGroup(cur, k)

            centinail = ListNode(-1)
            prev, cur, last = head, head, head
            while count:
                if prev is not cur:
                    centinail.next, cur = cur, cur.next, 
                    centinail.next.next, prev = prev, centinail.next
                else:
                    centinail.next, cur = prev, cur.next
                count -= 1
            last.next = newCur
            return centinail.next
        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                temp, head.next, cur = head.next, cur, head # insert the head before cur
                head = temp # move head to 
                count -= 1
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
        self.assertTrue(solution.convertListToArray(solution.reverseKGroup(head, 3)) == [3, 2, 1, 4, 5])        

if __name__ == "__main__" : unittest.main()
