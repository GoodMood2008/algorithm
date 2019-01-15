#!/user/bin/python
#-*- coding:utf-8 -*-

# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def makeTreeNode(self, array, length, node, i):
        left = 2*i + 1
        right = 2*i + 2
        if left < length and array[left]:
            node.left = self.makeTreeNode(array, length, TreeNode(array[left]), left)
        if right < length and array[right]:
            node.right = self.makeTreeNode(array, length, TreeNode(array[right]), right)
        return node

    def convertArrayToTree(self, array):
        if not array:
            return None
        return self.makeTreeNode(array, len(array), TreeNode(array[0]), 0)

    def printTree(self, root):

        if (root == None):
            return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



#Given a binary tree, return the inorder traversal of its nodes' values.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [1,None,2, None, None, 3]
        tree = solution.convertArrayToTree(array)
        result = solution.inorderTraversal(tree)
        self.assertTrue(result == [1, 3, 2])

if __name__ == "__main__" : unittest.main()
