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
        result = list(map(lambda r : self.traverseBFS(r), self.generateSubTrees(range(1, n + 1))))
        print(result)
        return result


    def generateSubTrees(self, values):
        if not values:
            return [None]
        result = []
        for value in values:
            left = self.generateSubTrees(filter(lambda v : v < value, values))
            right = self.generateSubTrees(filter(lambda v : v > value, values))
            for l1 in left:
                for r1 in right:
                    node = TreeNode(value)
                    node.left = TreeNode(None) if l1 == None and r1 != None else l1
                    node.right = TreeNode(None) if l1 != None and r1 == None else r1
                    result.append(node)
        return result

    def traverseBFS(self, root):
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

        self.assertTrue(solution.generateTrees(3) == output)

if __name__ == "__main__" : unittest.main()
