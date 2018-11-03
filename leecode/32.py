#!/user/bin/python
#-*- coding:utf-8 -*-



class Solution:
    # bruth-forth
    # T(n) = O(n^3)
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        length = len(s)
        for i in range(length - 1):
            for j in range(i+1, length):
                if self.isValid(s, i, j):
                    validLenth = j - i + 1
                    maxlength = maxlength if validLenth < maxlength else validLenth
        return maxlength

    def isValid(self, s, i, j):
        stack = []
        for ele in range(i, j + 1):
            if s[ele] == '(':
                stack.append(s[ele])
            elif s[ele] == ')':
                if len(stack) == 0:
                    return False
                else:
                    if (stack.pop() != '('):
                        return False
        return len(stack) == 0    

    #dynamic programming
    #T(n) = O(n)
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        length = len(s)
        d = [0] * length
        for i in range(1, length):
            if s[i] == ')':
                if s[i - 1] == '(':
                    d[i] = 2 if i < 2 else d[i - 2] + 2
                else:
                    if i - d[i - 1] - 1 >= 0 and s[i - d[i - 1] - 1] == '(':
                        if i - d[i - 1] - 1 > 0:
                            d[i] = d[i - 1] + d[i - d[i - 1] - 2] + 2
                        else: 
                            d[i] = d[i - 1] + 2
                maxLength = maxLength if maxLength > d[i] else d[i]
        return maxLength


    #dynamic programming
    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    maxLength = maxLength if maxLength > length else length
        return maxLength




#Example:
#"((())"

#(( --> invalid
#(( --> invalid
#() --> valid, length=2
#)) --> invalid
#((()--> invalid
#(())--> valid, length=4
#maxlength=4
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.longestValidParentheses("((") == 0)
        self.assertTrue(solution.longestValidParentheses("((()") == 2)
        self.assertTrue(solution.longestValidParentheses("(())") == 4)
        self.assertTrue(solution.longestValidParentheses1("((") == 0)
        self.assertTrue(solution.longestValidParentheses1("((()") == 2)
        self.assertTrue(solution.longestValidParentheses1("(())") == 4)
        self.assertTrue(solution.longestValidParentheses2("((") == 0)
        self.assertTrue(solution.longestValidParentheses2("((()") == 2)
        self.assertTrue(solution.longestValidParentheses2("(())") == 4)        

if __name__ == "__main__" : unittest.main()
