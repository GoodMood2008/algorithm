#!/user/bin/python
#-*- coding:utf-8 -*-

#boyer-moore
class Solution:
    def search(self, inputStr, pattern):
        if len(inputStr) < len(pattern):
            return -1
        bc = self.generateBC(pattern)
        suffix, prefix = self.generateGoodSuffix(pattern)

        i = 0
        patternLength = len(pattern)
        while i <= len(inputStr) - patternLength:
            j = patternLength - 1
            while j >= 0:
                if inputStr[i+j] != pattern[j]:
                    break
                j -= 1
            if j < 0: # match
                return i
            # exist bad chracter, i + bad c
            x = j - bc[ord(inputStr[i + j]) - ord('a')]
            #exist good suffix
            y = 0
            if j < patternLength - 1:
                y = moveByGoodSuffix(j, patternLength, suffix, prefix)
            i = i + max(x, y)
        return -1

    #主流程代码中，关于while循环的这段比较难以理解，为何是j+2
    def moveByGoodSuffix(j, length, suffix, prefix):
        k = length - 1 - j # length of good suffix
        if suffix[k] != -1:
            return j - suffix[k] + 1
        r = j + 2 # 这个地方是个难度
        while r < length - 1:
            if prefix[length - r + 1]:
                return r
            ++r
        return length


    #使用了散列表
    def generateBC(self, m):
        bc = [-1] * 26
        for i in range(len(m)):
            bc[ord(m[i]) - ord('a')] = i        
        return bc

    #
    #output index： 以长度计算的数组，表示后缀的长度
    #       suffix: 后缀的位置，值为位置
    #       prefix：是否有前缀，值为true/false
    #算法比较巧妙
    def generateGoodSuffix(self, m):
        length = len(m)
        suffix = [-1] * length
        prefix = [False] * length
        for i in range(length - 1):
            j = i
            k = 0
            while j>=0 and m[j] == m[length - 1 - k]:
                j -= 1
                k += 1
            if k: suffix[k] = j + 1
            if j == -1: prefix[k] = True
        return (suffix, prefix)


import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.search("abdacabdc", "aca") == 3)


if __name__ == "__main__" : unittest.main()
