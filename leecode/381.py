#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i&(i-1)] + 1
        print(result)
        return result


#Given a non negative integer number num. 
#For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in 
#their binary representation and return them as an array.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.countBits(2) == [0,1,1])
        self.assertTrue(solution.countBits(5) == [0,1,1,2,1,2])




if __name__ == "__main__" : unittest.main()
