#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution:

    # T(n) = O(len(strs) * len(strs[0]))
    # S(n) = O(len(str[0]))
    def longestCommonPrefix(self, strs):
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

    

import unittest
class SolutionTestCase(unittest.TestCase):
    def testMatch(self):
        solution = Solution()
        self.assertTrue(solution.longestCommonPrefix(["flower","flow","flight"]) == "fl")
        self.assertTrue(solution.longestCommonPrefix(["dog","racecar","car"]) == "")

if __name__ == "__main__": unittest.main()