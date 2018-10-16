#/user/bin/python
#-*- coding:utf-8 -*-


# 用暴力穷举的方法，或者分治法，计算得到的复杂度为omiga(3^n)
# 而backtracking，复杂度这里同样是O(3^m*4^n) m+n = len(digits)
class Solution(object):
    def getSymbols(self, symbol):
        if "2" == symbol:
            return ["a","b","c"]
        elif "3" == symbol:
            return ["d","e","f"]
        elif "4" == symbol:
            return ["g","h","i"]
        elif "5" == symbol:
            return ["j","k","l"]
        elif "6" == symbol:
            return ["m","n","o"]
        elif "7" == symbol:
            return ["p","q","r","s"]
        elif "8" == symbol:
            return ["t","u","v"]
        elif "9" == symbol:
            return ["w","x","y","z"]
        else:
            raise Exception("not wanted result")

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """        
        result = []
        self.backtraking(result, digits, [], 0)
        return result
        
    ##
    def backtraking(self, alist, digits, cur, index):
        if index == len(digits):
            if len(cur) != 0:
                alist.append("".join(cur))
            return
        symbols = self.getSymbols(digits[index])
        for symbol in symbols:
            next = cur + [symbol]
            self.backtraking(alist, digits, next, index + 1)    





import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self):
        solution = Solution()
        self.assertTrue(solution.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertTrue(solution.letterCombinations("") == [])

if __name__ == "__main__" : unittest.main()