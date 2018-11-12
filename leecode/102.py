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

    # BFS T(n) = O(n)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = list()

        queue = list()
        queue.append(root)
        visited = set()
        visited.add(root)

        while queue:
            self.appendQueue(queue, result)
            queue = self.getNextLevelNodes(queue)
        return result

    def appendQueue(self, queue, result):
        result.append([])
        for node in queue:
            result[-1].append(node.val)    

    def getNextLevelNodes(self, queue):
        result = []
        for node in queue:
            for subNode in [node.left, node.right]:
                if None != subNode:
                    result.append(subNode)
        return result
        















    # DFS T(n) = O(n)
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = list()
        visited = set()
        self.orderByLevel(root, 0, visited, result)
        return result

    def orderByLevel(self, root, level, visited, result):
        visited.add(root)
        self.append(result, level, root.val)
        for node in [root.left, root.right]:
            if None != node and node not in visited:
                self.orderByLevel(node, level + 1, visited, result)   

    def append(self, result, level, value):
        if level >= len(result):
            for _ in range(len(result), level + 1):
                result.append([])
        result[level].append(value)










#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        array = [3,9,20,None,None,15,7]
        tree = solution.convertArrayToTree(array)
        self.assertTrue(solution.levelOrder(tree) == [[3], [9,20], [15,7]])



if __name__ == "__main__" : unittest.main()
