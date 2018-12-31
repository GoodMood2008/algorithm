#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.pie = set()
        self.na = set()
        self.col = set()
        self.result = 0
        self.dfs(0, [], n)
        return self.result

    def dfs(self, row, seq, n):
        if row >= n:
            self.result += 1
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



    def totalNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = 0
        self.n = n
        self.dfs1([], [], [])
        return self.result

    def dfs1(self, queens, xy_dif, xy_sum):
        row = len(queens)
        if row >= self.n:
            self.result += 1
            return
        for col in range(self.n):
            if col not in queens and row + col not in xy_sum and row - col not in xy_dif:
                self.dfs1(queens + [col], xy_dif + [row - col], xy_sum + [row + col])


    # bit count accelerate
    def totalNQueens2(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.count = 0
        self.n = n
        self.dfs2(0, 0, 0, 0)
        return self.count

    def dfs2(self, row, col, pie, na):
        if row >= self.n:
            self.count += 1
            return

        bits = (~(col|pie|na)) & ((1 << self.n) - 1)
        while bits:
            p = bits & (-bits)
            self.dfs2(row+1, col|p, (pie|p)<<1, (na|p)>>1)
            bits &= (bits - 1)


#The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.totalNQueens(4) ==  2)
        self.assertTrue(solution.totalNQueens1(4) ==  2)
        self.assertTrue(solution.totalNQueens2(4) ==  2)

if __name__ == "__main__" : unittest.main()

