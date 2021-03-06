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

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:return []
        result = list()

        queue = collections.deque()
        queue.append(root)

        while queue:
            result.append([]) 
            size = len(queue)   
            for i in range(size):
                node = queue.popleft()
                result[-1].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right) 
        return result


        















    # DFS T(n) = O(n)
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = list()
        self.orderByLevel(root, 0)
        return self.result

    def orderByLevel(self, node, level):
        if None == node:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        self.orderByLevel(node.left, level + 1)
        self.orderByLevel(node.right, level + 1)
 











#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [3,9,20,None,None,15,7]
        tree = solution.convertArrayToTree(array)
        self.assertTrue(solution.levelOrder(tree) == [[3], [9,20], [15,7]])
        self.assertTrue(solution.levelOrder1(tree) == [[3], [9,20], [15,7]])


if __name__ == "__main__" : unittest.main()
