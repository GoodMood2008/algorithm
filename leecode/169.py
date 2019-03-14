#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        for i in range(int(len(s)/2)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1],s[i]

             
        


#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        inputStr = ["h","e","l","l","o"]
        solution.reverseString(inputStr)
        self.assertTrue(inputStr == ["o","l","l","e","h"])

        inputStr = ["H","a","n","n","a","h"]  
        solution.reverseString(inputStr)
        self.assertTrue(inputStr == ["h","a","n","n","a","H"])      

if __name__ == "__main__" : unittest.main()
