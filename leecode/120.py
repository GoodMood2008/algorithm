#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    #T(n) = O(2^n) n is len(triangle)
    #O(n) = O(2^n) n is len(triangle)
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        temp = []
        lenth = len(triangle)
        for _ in range(lenth):
            temp.append([])
        for i in reversed(range(lenth)):
            for j in range(len(triangle[i])):
                if i == lenth - 1:
                    temp[i].append(triangle[i][j])
                else:
                    temp[i].append(min(temp[i+1][j], temp[i+1][j+1]) + triangle[i][j])
        return temp[0][0]            

    #Bruth Forch
    #T(n) = O(n!) n is len(triangle)
    #S(n) = O(1)
    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0

        self.minpath = '#'
        self.dfs(triangle, triangle[0][0], 0, 0)
        return self.minpath

    def dfs(self, triangle, sumValue, i, j):
        if i == len(triangle) - 1:
            self.minpath = sumValue if self.minpath == '#' else min(self.minpath, sumValue)
            return
        self.dfs(triangle, sumValue + triangle[i+1][j], i + 1, j)
        self.dfs(triangle, sumValue + triangle[i+1][j + 1], i + 1, j + 1)



import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        input = [[2], 
                  [3,4],
                  [6,5,7],
                  [4,1,8,3]]
        self.assertTrue(solution.minimumTotal(input) == 11)
        self.assertTrue(solution.minimumTotal1(input) == 11)
        input = [[2], 
                  [6,4],
                  [6,5,3],
                  [4,1,10,10]]
        self.assertTrue(solution.minimumTotal(input) == 12)
        self.assertTrue(solution.minimumTotal1(input) == 12)

if __name__ == "__main__" : unittest.main()