#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """ 
        if not matrix or not matrix[0]: return 0

        self.direction = [(-1,0),(1,0),(0,-1),(0,1)]
        self.hight,self.width = len(matrix), len(matrix[0])
        self.count = 0

        for i in range(self.hight):
            for j in range(self.width):
                self.dfs(matrix, i, j, [], 0)
        return self.count

    def dfs(self, matrix, i, j, path, count):
        if i < 0 or i >= self.hight or j < 0 or j >= self.width:
            return

        value = matrix[i][j]
        if path and value <= path[-1]:
            self.count = max(self.count, count)
            return

        for i1, j1 in self.direction:
            self.dfs(matrix, i + i1, j + j1, path + [value], count + 1)

#You are given coins of different denominations and a total amount of money amount. 
#Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        input = [[3,4,5],
                  [3,2,6],
                  [2,2,1]]
        self.assertTrue(solution.longestIncreasingPath(input) == 4)
        input = [[9,9,4],
                  [6,6,8],
                  [2,1,1]] 
        self.assertTrue(solution.longestIncreasingPath(input) == 4)
        input = [[0],[1],[5],[5]]
        self.assertTrue(solution.longestIncreasingPath(input) == 3)

if __name__ == "__main__" : unittest.main()