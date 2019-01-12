#!/user/bin/python
#-*- coding:utf-8 -*-
import collections

class Solution:
    #kahn algorithm
    import collections
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #construct adj table
        adj = dict()
        for i in range(numCourses):
            adj.update({i:list()})
        for x, y in prerequisites:
            adj.get(x).append(y) 
        #statistic indegree
        indegree = [0 for _ in range(numCourses)]
        for i in adj:
            for j in adj.get(i):
                indegree[j] += 1
        #queue of indegree equal 0
        dq = collections.deque()
        for i, v in enumerate(indegree):
            if not v:
                dq.append(i)
        # the main program   
        result = []
        while dq:
            p = dq.popleft()
            result.append(p)
            for j in adj.get(p):
                indegree[j] -= 1
                if not indegree[j]:
                    dq.append(j)
        return list(reversed(result)) if len(result) == numCourses else []


    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #construct adj table
        self.adj = dict()
        for i in range(numCourses):
            self.adj.update({i:list()})
        for x, y in prerequisites:
            self.adj.get(x).append(y) 

        self.result = []
        self.visited = [False] * numCourses
        self.onStack = [False] * numCourses
        for i in range(numCourses):
            if not self.visited[i] and self.dfs(i):
                return []
        return self.result

    def dfs(self, i):
        if self.visited[i]: return False
        self.visited[i] = self.onStack[i] = True
        for j in self.adj[i]:
            if self.onStack[j] or self.dfs(j): 
                return True
        self.onStack[i] = False
        self.result.append(i)
        return False


#There are a total of n courses you have to take, labeled from 0 to n-1.
#Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        self.assertTrue(solution.findOrder(2, [[1,0]]) == [0, 1])
        self.assertTrue(solution.findOrder(2, [[1,0],[0,1]]) == [])
        self.assertTrue(solution.findOrder(3, [[0,2],[1,2],[2,0]]) == [])
        self.assertTrue(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3])
        self.assertTrue(solution.findOrder1(2, [[1,0]]) == [0, 1])
        self.assertTrue(solution.findOrder1(2, [[1,0],[0,1]]) == [])
        self.assertTrue(solution.findOrder1(3, [[0,2],[1,2],[2,0]]) == [])
        self.assertTrue(solution.findOrder1(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3])

if __name__ == "__main__" : unittest.main()