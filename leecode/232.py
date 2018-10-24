#!/user/bin/python
#-*- coding:utf-8 -*-

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.output:  # not has element, put input to output reversely
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop() if self.output else None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.output:  # not has element, put input to output reversely
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1] if self.output else None        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.input or self.output else True



#Given a linked list, determine if it has a cycle in it.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertTrue(queue.pop() == 1)
        queue.push(3)
        self.assertTrue(queue.pop() == 2)
        self.assertTrue(not queue.empty())
        self.assertTrue(queue.pop() == 3)
        self.assertTrue(queue.empty())

if __name__ == "__main__" : unittest.main()
