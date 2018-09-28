#!/user/bin/python
#-*- coding:utf-8 -*-

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.

#num range from 1 to 3999
class Solution:
    def thousand(self, n) :
        return 'M'*n

    def nums(self, n, ch1, ch5, ch10):
        if n == 0:
            return ''
        elif n < 4:
            return ch1 * n
        elif n == 4:
            return ch1 + ch5
        elif n < 9:
            return ch5 + ch1 * (n - 5)
        else: 
            return ch1 + ch10        

    def handred(self, n):
        return self.nums(n, 'C', 'D', 'M')

    def ten(self, n):
        return self.nums(n, 'X', 'L', 'C')

    def num(self, n):
        return self.nums(n, 'I', 'V', 'X')

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.thousand(int(num/1000)) + self.handred(int(num/100)%10) + self.ten(int(num/10)%10) + self.num(num%10)



import unittest
class SolutionTestCase(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.intToRoman(3) == "III")
        self.assertTrue(solution.intToRoman(9) == "IX")
        self.assertTrue(solution.intToRoman(58) == "LVIII")
        self.assertTrue(solution.intToRoman(1994) == "MCMXCIV")

if __name__ == "__main__" : unittest.main()