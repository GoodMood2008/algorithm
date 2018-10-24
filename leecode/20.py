#!/usr/bin/python
#-*- coding:utf-8 -*-

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        symbols = {'}':'{', ')':'(', ']':'['}
        for c in s:
            if c not in symbols:
                st.append(c)
            elif not st or symbols[c] != st.pop():
                return False
        return not st


        

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.isValid("()[]{}"))
        self.assertTrue(not solution.isValid("(]"))
        self.assertTrue(not solution.isValid("([)]"))
        self.assertTrue(solution.isValid("{[]}"))
        self.assertTrue(not solution.isValid("((("))

if __name__ == "__main__": unittest.main()