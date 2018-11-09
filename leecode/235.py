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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor1(self, root, p, q):         
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array =  [6,2,8,0,4,7,9,None,None,3,5]
        tree = solution.convertArrayToTree(array)
        self.assertTrue(solution.lowestCommonAncestor(tree, tree.left, tree.right).val == 6)
        self.assertTrue(solution.lowestCommonAncestor(tree, tree.left, tree.left.right).val == 2)
        self.assertTrue(solution.lowestCommonAncestor1(tree, tree.left, tree.right).val == 6)
        self.assertTrue(solution.lowestCommonAncestor1(tree, tree.left, tree.left.right).val == 2)


if __name__ == "__main__" : unittest.main()
