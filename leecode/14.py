#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution:

    # T(n) = O(len(strs) * len(strs[0]))
    # S(n) = O(len(str[0]))
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        result = []
        for i in range(len(strs[0])):
            c = strs[0][i]
            if all(map(lambda str: False if (len(str) < (i + 1)) else (str[i] == c), strs)):
                result.append(c)
            else:
                break
        return ''.join(result)

    

    #divide and conquer
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        length = len(strs)
        comPrefix1 = self.longestCommonPrefix(strs[0 : int(length/2)])
        comPrefix2 = self.longestCommonPrefix(strs[int(length/2) : ])
        len1 = len(comPrefix1)
        len2 = len(comPrefix2)
        # if one is empty, return ''
        if 0 == len1 or 0 == len2:
            return ''
        # make comPrefix1 samller
        if len1 > len2:
            comPrefix1, comPrefix2 = comPrefix2, comPrefix1
        # get the common prefix
        result = []
        for i in range(len(comPrefix1)):
            if comPrefix1[i] == comPrefix2[i]:
                result.append(comPrefix1[i])
            else:
                break
        return ''.join(result)        





import unittest
class SolutionTestCase(unittest.TestCase):
    def testMatch(self):
        solution = Solution()
        self.assertTrue(solution.longestCommonPrefix(["flower","flow","flight"]) == "fl")
        self.assertTrue(solution.longestCommonPrefix(["dog","racecar","car"]) == "")

if __name__ == "__main__": unittest.main()