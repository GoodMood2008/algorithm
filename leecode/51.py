#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.pie = set()
        self.na = set()
        self.col = set()
        self.result = []
        self.dfs(0, [], n)
        return [[''.join(['.' if c != i else 'Q' for i in range(n)]) for c in seq] for seq in self.result]

    def dfs(self, row, seq, n):
        if row >= n:
            self.result.append(seq)
            return
        for col in range(n):
            if col in self.col or row + col in self.pie or row - col in self.na:
                continue
            self.pie.add(row + col)
            self.na.add(row - col)
            self.col.add(col)
            self.dfs(row + 1, seq + [col], n)
            self.pie.remove(row + col)
            self.na.remove(row - col)
            self.col.remove(col)



    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.dfs1([], [], [], result, n)
        return [[''.join(['.' if c != i else 'Q' for i in range(n)]) for c in seq] for seq in result]

    def dfs1(self, queens, xy_dif, xy_sum, result, n):
        row = len(queens)
        print(row, " ", queens, " ", xy_dif, " ", xy_sum)
        if row >= n:
            result.append(queens)
            return
        for col in range(n):
            if col not in queens and row + col not in xy_sum and row - col not in xy_dif:
                self.dfs1(queens + [col], xy_dif + [row - col], xy_sum + [row + col], result, n)



#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.solveNQueens(4) ==  [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
        self.assertTrue(solution.solveNQueens1(4) ==  [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

if __name__ == "__main__" : unittest.main()

