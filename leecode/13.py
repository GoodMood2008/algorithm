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
#12 是13的一个前导，如果没有12，仅仅考虑13，思路会很困难，如果先做12， 再考虑13，则仅仅逆向推导即可
class Solution:
    def parseThousand(self, s) :
        return self.parseRepeat(s, 'M')

    def parseRepeat(self, s, ch):
        result = 0
        pos = 0
        while pos < len(s):
            if s[pos] != ch:
                break
            result += 1
            pos += 1
        return pos, result

    def parseRepeatWithoutPos(self, s, ch):
        pos, value = self.parseRepeat(s, ch)
        return value


    def parseNumStr(self, s, pos, chs):
        strTemp = ''
        newpos = pos
        while newpos < len(s):
            if s[newpos] not in chs:
                break
            strTemp = strTemp + s[newpos]
            newpos += 1
        return newpos, strTemp


    def parseNumbers(self, s, pos, ch1, ch5, ch10):
        newpos, strTemp = self.parseNumStr(s, pos, [ch1, ch5, ch10])

        if 0 == len(strTemp):
            return newpos, 0
            
        if (ch1 + ch10) == strTemp :
            return newpos, 9
        elif (ch1 + ch5) == strTemp:
            return newpos, 4
        elif ch5 == strTemp[0]:
            return newpos, 5 + self.parseRepeatWithoutPos(strTemp[1:], ch1)
        else:
            return newpos, self.parseRepeatWithoutPos(strTemp, ch1)           

    def parseHandred(self, s, pos):
        return self.parseNumbers(s, pos, 'C', 'D', 'M')

    def parseTen(self, s, pos):
        return self.parseNumbers(s, pos, 'X', 'L', 'C')
     
    def parseNum(self, s, pos):
        return self.parseNumbers(s, pos, 'I', 'V', 'X')


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        pos = 0
        pos, value = self.parseThousand(s)
        result += 1000 * value
        pos, value = self.parseHandred(s, pos)
        result += 100 * value
        pos, value = self.parseTen(s, pos)
        result += 10 * value
        pos, value = self.parseNum(s, pos)
        result += value
        return result


import unittest
class SolutionTestCase(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.romanToInt("III") == 3)
        self.assertTrue(solution.romanToInt("IX") == 9)
        self.assertTrue(solution.romanToInt("LVIII") == 58)
        self.assertTrue(solution.romanToInt("MCMXCIV") == 1994)

if __name__ == "__main__" : unittest.main()