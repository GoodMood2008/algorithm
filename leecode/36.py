#!/user/bin/python
#-*- coding:utf-8 -*-



class Solution:
    def __init__(self):
        self.validNums = ["1","2", "3", "4", "5", "6", "7", "8", "9"]

    def isValid(self, eles):
        if len(eles) != 9:
            return False
        nums = set()
        for ele in eles:
            if not ele.isdigit():
                continue
            if ele in self.validNums and ele not in nums:
                nums.add(ele)
            else:
                print("False", nums)
                return False
        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        board_trans = []
        board_little = []
        for i in range(9):
            board_trans.append([])
            board_little.append([])
        for i in range(9):
            for j in range(9):
                board_trans[j].append(board[i][j])
                board_little[int(i/3) + int(j/3)*3].append(board[i][j])
        return all([self.isValid(ele) for ele in board]) and all([self.isValid(ele) for ele in board_trans]) and all([self.isValid(ele) for ele in board_little])


    # board is 9*9 ele is 1-9 and .
    def isValidSudoku1(self, board):
        cols = []
        rows = []
        squares = []
        for _ in range(9):
            cols.append(list())
            rows.append(list())
            squares.append(list())
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])
                index = 3*int(j/3) + int(i/3)
                if board[i][j] in squares:
                    return False
                else:
                    squares[index].append(board[i][j])
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
        self.assertTrue(solution.isValidSudoku(inputdata))
        self.assertTrue(solution.isValidSudoku1(inputdata))
      
if __name__ == "__main__" : unittest.main()
