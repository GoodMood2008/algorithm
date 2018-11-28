#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == None:
            return True
        if None == board or 0 == len(board) or 0 == len(board[0]):
            return False
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, 0):
                        return True
        return False

    def dfs(self, board, word, i, j, pos):
        if pos >= len(word):
            return True
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        if board[i][j] == word[pos]:
            temp, board[i][j] = board[i][j], '#'
            result = self.dfs(board, word, i + 1, j, pos + 1) or \
                     self.dfs(board, word, i - 1, j, pos + 1) or \
                     self.dfs(board, word, i, j + 1, pos + 1) or \
                     self.dfs(board, word, i, j - 1, pos + 1)
            board[i][j] = temp
            return result
        return False



#The word can be constructed from letters of sequentially adjacent cell, 
#where "adjacent" cells are those horizontally or vertically neighboring. 
#The same letter cell may not be used more than once.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        board = [ ['A','B','C','E'],
                  ['S','F','C','S'],
                  ['A','D','E','E']]
        self.assertTrue(solution.exist(board, "ABCCED"))
        self.assertTrue(solution.exist(board, "SEE"))
        self.assertTrue(not solution.exist(board, "ABCB"))

if __name__ == "__main__" : unittest.main()