#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution:
    # T(N) = O(NlogN)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    # T(n) = O(n)
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sArr, tArr = [0]*26, [0]*26
        for c in s:
            sArr[ord(c) - ord('a')] += 1
        for c in t:
            tArr[ord(c) - ord('a')] += 1
        return sArr == tArr    
        

#Given two strings s and t , write a function to determine if t is an anagram of s.
#You may assume the string contains only lowercase alphabets.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(not solution.isAnagram("rat", "car"))
        self.assertTrue(solution.isAnagram("anagram", "nagaram"))
        self.assertTrue(not solution.isAnagram1("rat", "car"))
        self.assertTrue(solution.isAnagram1("anagram", "nagaram"))



if __name__ == "__main__" : unittest.main()
