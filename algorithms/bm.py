#!/user/bin/python
#-*- coding:utf-8 -*-

#boyer-moore
class Solution:
    def search(self, inputStr, pattern):
        if len(inputStr) < len(pattern):
            return -1
        bc = self.generateBC(pattern)
        i = 0
        patternLength = len(pattern)
        while i <= len(inputStr) - len(pattern):
            j = patternLength - 1
            while j >= 0:
                if inputStr[i+j] != pattern[j]:
                    break
                j -= 1
            if j < 0: # match
                return i
            # exist bad chracter, i + bad c
            i = i + (j - bc[ord(inputStr[i + j]) - ord('a')])
        return -1

    def generateBC(self, m):
        bc = [-1] * 26
        for i in range(len(m)):
            bc[ord(m[i]) - ord('a')] = i        
        return bc

    def generateGoodSuffix(self, m):
        length = len(m)
        suffix = [-1] * length
        prefix = [False] * length
        for i in range(length):
            j = i
            k = 0
            while j>=0 and b[j] == b[length - 1 - k]:
                j -= 1
                k += 1
            if not k: suffix[k] = j + 1
            if j == -1: prefix[k] = True
        return (suffix, prefix)


import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.search("abdacabdc", "aca") == 3)


if __name__ == "__main__" : unittest.main()
