#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution(object):
    def reverseWords(self, s:'str') -> 'str':
                  
        


#A word is defined as a sequence of non-space characters.
#Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
#You need to reduce multiple spaces between two words to a single space in the reversed string.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.majorityElement("the sky is blue") == "blue is sky the")

if __name__ == "__main__" : unittest.main()
