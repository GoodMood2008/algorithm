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

    # BFS T(n) = O(n)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:return 0
        result = 0

        queue = collections.deque()
        queue.append(root)

        while queue:
            result += 1 
            size = len(queue)   
            for i in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) 
        return result


    # DFS T(n) = O(n)
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.orderByLevel(root, 0)
        return self.depth + 1

    def orderByLevel(self, node, level):
        if None == node:
            return
        if self.depth < level:
            self.depth = level
        self.orderByLevel(node.left, level + 1)
        self.orderByLevel(node.right, level + 1)
 











#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [3,9,20,None,None,15,7]
        tree = solution.convertArrayToTree(array)
        self.assertTrue(solution.maxDepth(tree) == 3)
        self.assertTrue(solution.maxDepth1(tree) == 3)


if __name__ == "__main__" : unittest.main()
