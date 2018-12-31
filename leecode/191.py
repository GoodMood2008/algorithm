#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        temp = n
        while temp:
            temp = temp & (temp - 1)
            count += 1
        return count




import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.hammingWeight(0b00000000000000000000000000001011) == 3)
        self.assertTrue(solution.hammingWeight(0b00000000000000000000000010000000) == 1)
        self.assertTrue(solution.hammingWeight(0b11111111111111111111111111111101) == 31)


if __name__ == "__main__" : unittest.main()