#!/user/bin/python
#-*- coding:utf-8 -*-
import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = [[] for _ in range(numCourses)]
        self.visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            self.graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True
        self.visit[i] = -1
        for j in self.graph[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True    



    def canFinish1(self, numCourses, prerequisites):
        # construct adjacenct table
        courses = dict()
        for prerequisite in prerequisites:
            if None == courses.get(prerequisite[0]):
                courses.update({prerequisite[0]:list()})
            courses.get(prerequisite[0]).append(prerequisite[1])
        for key in courses.keys():
            if not self.dfs1(numCourses, [], key, courses):
                return False
        return True


    def dfs1(self, numCourses, visted, k, courses):
        if len(visted) == numCourses or k in visted:
            return False
        if k not in courses:
            return True
        for key in courses.get(k):
            if not self.dfs1(numCourses, visted + [k], key, courses):
                return False
        return True
    

    #kahn algorithm
    import collections
    def canFinish2(self, numCourses, prerequisites):
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
        count = 0
        print(adj, " ", dq)
        while dq:
            p = dq.popleft()
            count += 1
            for j in adj.get(p):
                indegree[j] -= 1
                if not indegree[j]:
                    dq.append(j)
        print(count)
        return count == numCourses




#The input prerequisites is a graph represented by a list of edges, 
#not adjacency matrices. Read more about how a graph is represented.
#You may assume that there are no duplicate edges in the input prerequisites.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        self.assertTrue(solution.canFinish(2, [[1,0]]))
        self.assertTrue(not solution.canFinish(2, [[1,0],[0,1]]))
        self.assertTrue(solution.canFinish1(2, [[1,0]]))
        self.assertTrue(not solution.canFinish1(2, [[1,0],[0,1]]))
        self.assertTrue(solution.canFinish2(2, [[1,0]]))
        self.assertTrue(not solution.canFinish2(2, [[1,0],[0,1]]))

if __name__ == "__main__" : unittest.main()