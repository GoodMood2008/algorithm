#!/usr/bin/python
#-*- coding:utf-8 -*-

#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.length = n
        self.generate("", 0, 0)
        return self.result

    #T(n) < O(2^2n)
    def generate(self, s, left, right):
        print(s, " ", left, " ", right)
        if left == self.length and right == self.length:
            self.result.append(s)
        if left < self.length:
            self.generate(s+'(', left+1, right)
        if right < left:
            self.generate(s+')', left, right+1)

        

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"])

if __name__ == "__main__": unittest.main()