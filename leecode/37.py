#!/user/bin/python
#-*- coding:utf-8 -*-



class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if None == board or len(board) == 0:
            return False
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    for c in ['1','2','3','4','5','6', '7', '8', '9']:
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if (self.solve(board)):
                                return True
                            else:
                                board[i][j] = '.'
        return False

    def isValid(self, board, row, col, c):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if i == row and board[i][j] == c:
                    return False
                if j == col and board[i][j] == c:
                    return False

                row_min = int(row/3) * 3
                col_min = int(col/3) * 3
                if row_min <= i < (row_min + 3) and \
                   col_min <= j < (col_min + 3) and \
                   board[i][j] == c:
                   return False
        return True



#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        inputdata = [["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]
        outputdata = [["5","3","4","6","7","8","9","1","2"],
                      ["6","7","2","1","9","5","3","4","8"],
                      ["1","9","8","3","4","2","5","6","7"],
                      ["8","5","9","7","6","1","4","2","3"],
                      ["4","2","6","8","5","3","7","9","1"],
                      ["7","1","3","9","2","4","8","5","6"],
                      ["9","6","1","5","3","7","2","8","4"],
                      ["2","8","7","4","1","9","6","3","5"],
                      ["3","4","5","2","8","6","1","7","9"]]
        self.assertTrue(not solution.isValid(inputdata, 0, 2, '8'))
        self.assertTrue(not solution.isValid(inputdata, 0, 2, '5'))
        self.assertTrue(solution.isValid(inputdata, 0, 2, '4'))
        self.assertTrue(solution.solveSudoku(inputdata))
        self.assertTrue(intput == outputdata)

      
if __name__ == "__main__" : unittest.main()
