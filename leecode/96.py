#!/user/bin/python
#-*- coding:utf-8 -*-

import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #T(n) = O(n^n)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 0
        return len(self.generateSubTrees(1, n))


    def generateSubTrees(self, start, end):
        if start >= end:
            return [None]
        result = []
        for v in range(start, end + 1):
            left = self.generateSubTrees(start, v - 1)
            right = self.generateSubTrees(v + 1, end)
            for l1 in left:
                for r1 in right:
                    result.append(v)
        return result

    #G(n): the number of unique BST for a sequence of length n.
    #F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.    
    #F(i, n) = G(i-1) * G(n-i)   1 <= i <= n 
    #G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 0
        if n == 1: return 1
        result = [0] * (n + 1)
        result[0], result[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                result[i] += result[j] * result[i - j - 1]
        return result[n]




    
#Given a binary tree, return the inorder traversal of its nodes' values.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(solution.numTrees(3) == 5)
        self.assertTrue(solution.numTrees1(3) == 5)


if __name__ == "__main__" : unittest.main()
