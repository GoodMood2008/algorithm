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


    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head: return None
        
        eleMap, cur = dict(), head
        while cur:
            if eleMap.get(cur.val):
                eleMap[cur.val] = eleMap.get(cur.val) + 1
            else:
                eleMap.update({cur.val:1})
            cur = cur.next
        repeats = [k for (k, v) in eleMap.items() if v > 1]

        sentinal = ListNode(-1)
        cur, tail = head, sentinal
        while cur:
            if cur.val not in repeats:
                tail.next = cur
                tail = tail.next
            cur = cur.next
        tail.next = None
        return sentinal.next




    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None

        centinel = ListNode(None)
        centinel.next, prev, cur = head, centinel, head
        while cur:
            while cur.next and cur.val == cur.next.val: #this is the main idea to treat the senario to simple
                cur = cur.next
            if prev.next == cur:
                prev = prev.next
            else:
                prev.next = cur.next
            cur = cur.next
        return centinel.next


# Given a sorted linked list, 
# delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
#Input: 1->2->3->3->4->4->5
#Output: 1->2->5

#Input: 1->1->1->2->3
#Output: 2->3

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1, 2, 3, 3, 4, 4, 5]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.deleteDuplicates(head)) == [1, 2, 5])
        array = [1, 1, 1, 2, 3]
        head = solution.convertArrayToList(array)
        self.assertTrue(solution.convertListToArray(solution.deleteDuplicates(head)) == [2, 3])        

if __name__ == "__main__" : unittest.main()
