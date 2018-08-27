#!/bin/bash/python
#-*-coding:utf-8 -*-

class Solution:
    def isPalinDrome(self, s):
        if len(s) <= 1:
            return True
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            for j in range(len(s) - i):
                strTemp = s[i:(i+1+j)]
                if self.isPalinDrome(strTemp):
                    result = strTemp if len(strTemp) > len(result) else result
        return result

    #-----------------------------------
    def getPalindrome(self, s, i, j):
        if i < 0 or j > (len(s) - 1):
            return ""
        while True:
            if s[i] != s[j]:
                return s[(i + 1):j] if j >= i + 1 else "" 
            if (i == 0) or (j == (len(s) - 1)):
                return s[i:(j + 1)]
            i -= 1
            j += 1
        return ""

    #O(n^2)
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: #长度为0
            return ""
        result = s[0]
        for i in range(len(s)):
            strTemp = self.getPalindrome(s, i, i + 1) #偶对称
            result = strTemp if len(strTemp) > len(result) else result
            strTemp = self.getPalindrome(s, i - 1, i + 1) #奇对称
            result = strTemp if len(strTemp) > len(result) else result               
        return result


    #------------------------------------
    def preProcess(self, s):
        newS = list()
        newS.append('$')
        newS.append('#')
        for i in range(len(s)):
            newS.append(s[i])
            newS.append('#')
        newS.append('^')
        return newS

    def calcPalindromeRadius(self, s):
        p = [0] * len(s)
        idPos = 0
        maxPos = 0
        for i in range(1, len(s) - 1):
            p[i] = min(p[2 * idPos - i], maxPos - i) if maxPos > i else 1
            while s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if (i + p[i]) > maxPos:
                maxPos = i + p[i]
                idPos = i
        return p

    def getPalindromeWithRadius(self, s, p):
        maxLen = 0
        index = 0
        for i in range(1, len(p) - 1):
            if (p[i] > maxLen):
                maxLen = p[i]
                index = i
        return s[int((index - maxLen)/2) : (int((index - maxLen)/2) + maxLen - 1)]

    #O(n) manacher
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        newS = self.preProcess(s)
        p = self.calcPalindromeRadius(newS)
        return self.getPalindromeWithRadius(s, p)





import unittest
class SolutionTestCase(unittest.TestCase):


    def testfindMedian(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome("aa"), "aa")
        self.assertEqual(solution.longestPalindrome("babad"), "bab")
        self.assertEqual(solution.longestPalindrome("a"), "a")
        self.assertEqual(solution.longestPalindrome("baab"), "baab")
        self.assertEqual(solution.longestPalindrome("caad"), "aa")
        self.assertEqual(solution.longestPalindrome("ccc"), "ccc")
        self.assertEqual(solution.longestPalindrome("cccc"), "cccc")

    def testfindMedian1(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome2("asfdafdafasdfsafafdasfafasdfafaffafdsafadsffasdccccadfafasfdasfafasdfasfasdfasfsfasdfasf"), "cccc")

if __name__ == "__main__": unittest.main()


