#!/user/bin/python
#-*- coding:utf-8 -*-

# Definition for a binary tree node.
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

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        array = self.inorder(root)
        return array == sorted(set(array))

    def inorder(self, root):
        if root == None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)    

                
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if root == None:
            return True
        if min != None and root.val <= min:
            return False
        if max != None and root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and  self.isValid(root.right, root.val, max)

        



#Given a binary tree, determine if it is a valid binary search tree (BST).

#Assume a BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [5,1,4,None,None,3,6]
        tree = solution.convertArrayToTree(array)
        solution.printTree(tree)
        self.assertTrue(not solution.isValidBST(tree))
        self.assertTrue(not solution.isValidBST1(tree))

if __name__ == "__main__" : unittest.main()
