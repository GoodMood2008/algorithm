#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        self.end_of_word = '#'

        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node[self.end_of_word] = self.end_of_word

        self.result = set()
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self.dfs(board, root, "", i, j)

        return sorted(list(self.result))

    def dfs(self, board, node, cur_word, i, j):

        if i < 0 or i >= self.m or j < 0 or j >= self.n or board[i][j] == '@':
            return

        cur_word += board[i][j]
        children = node.get(board[i][j])


        if None == children:
            return

        if self.end_of_word in children:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        self.dfs(board, children, cur_word, i + 1, j)
        self.dfs(board, children, cur_word, i - 1, j)
        self.dfs(board, children, cur_word, i, j + 1)
        self.dfs(board, children, cur_word, i, j - 1)
        board[i][j] = tmp    



#Each word must be constructed from letters of sequentially adjacent cell, 
#where "adjacent" cells are those horizontally or vertically neighboring. 
#The same letter cell may not be used more than once in a word.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        board = [['o','a','a','n'],
                 ['e','t','a','e'],
                 ['i','h','k','r'],
                 ['i','f','l','v']]
        self.assertTrue(solution.findWords(board, ["oath","pea","eat","rain"]) == ["eat","oath"])

if __name__ == "__main__" : unittest.main()