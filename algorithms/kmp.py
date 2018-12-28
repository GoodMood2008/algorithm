#!/user/bin/python
#-*- coding:utf-8 -*-

#kmp
class Solution:
    def search(self, inputStr, pattern):
        nexts = self.getNexts(pattern)
        j = 0
        for i in range(len(inputStr)):
            while j > 0 and inputStr[i] != pattern[j]:
                j = nexts[j-1] + 1
            if inputStr[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
        return -1    

    def getNexts(self, pattern):
        nexts = [-1] * len(pattern)
        k = -1
        for i in range(1, len(pattern)):
            while k != -1 and pattern[k+1] != pattern[i]:
                k = next[k]
            if pattern[k+1] == pattern[i]:
                k += 1
            nexts[i] = k
        return nexts

import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.search("abdacabdc", "aca") == 3)


if __name__ == "__main__" : unittest.main()
