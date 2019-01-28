#!/user/bin/python
#-*- coding:utf-8 -*-

import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        return self.generateSubTrees(1, n)


    def generateSubTrees(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        result = []
        for v in range(start, end + 1):
            left = self.generateSubTrees(start, v - 1)
            right = self.generateSubTrees(v + 1, end)
            for l1 in left:
                for r1 in right:
                    node = TreeNode(v)
                    node.left = l1
                    node.right = r1
                    result.append(node)
        return result        

    def convertArraysToTree(self, arrays):
        if not arrays:return []
        result = []
        for array in arrays:
            result.append(self.convertArrayToTree(array))
        return result

    def convertArrayToTree(self, array):
        if not array: return None
        head = array[0]
        self.convertArrayToSubTree([head], array, 1)
        return head

    def convertArrayToSubTree(self, leverNodes, array, n):
        nextLevelNodes = []
        for node in leverNodes:
            if n >= len(array):
                return
            node.left = None if not array[n] else TreeNode(array[n])
            n += 1
            if n >= len(array):
                return
            node.right = None if not array[n] else TreeNode(array[n])
            n += 1
            if node.left:
                nextLevelNodes.append(node.left)
            if node.right:
                nextLevelNodes.append(node.right)
        self.convertArrayToSubTree(nextLevelNodes, array, n)











    def generateTrees1(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = list(map(lambda r : self.traverseBFS1(r), self.generateSubTrees1(range(1, n + 1))))
        print(result)
        return result


    def generateSubTrees1(self, values):
        if not values:
            return [None]
        result = []
        for value in values:
            left = self.generateSubTrees1(filter(lambda v : v < value, values))
            right = self.generateSubTrees1(filter(lambda v : v > value, values))
            for l1 in left:
                for r1 in right:
                    node = TreeNode(value)
                    node.left = TreeNode(None) if l1 == None and r1 != None else l1
                    node.right = TreeNode(None) if l1 != None and r1 == None else r1
                    result.append(node)
        return result

    def traverseBFS1(self, root):
        dq = collections.deque()
        dq.append(root)
        result = []
        while dq:
            node = dq.popleft()
            if node.left != None:
                dq.append(node.left)
            if node.right != None:
                dq.append(node.right)
            if not dq and node.val == None: # dn't add the last None node
                continue
            result.append(node.val)
        return result



#Given a binary tree, return the inorder traversal of its nodes' values.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        output = [
                  [1,None,3,2],
                  [3,2,None,1],
                  [3,1,None,None,2],
                  [2,1,3],
                  [1,None,2,None,3]
                ]

        #self.assertTrue(solution.generateTrees1(3) == output)


if __name__ == "__main__" : unittest.main()
