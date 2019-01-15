#!/user/bin/python
#-*- coding:utf-8 -*-

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :org: List[int]
        :seqs: List[List[int]]
        """
        if not org: return False

        # construct ingress table
        ingress = [0]*len(org)
        inverseAdj = dict()
        count = 0
        for i, j in seqs:
            if not inverseAdj.get(j):
                inverseAdj.update({j:set()})
                count += 1
            inverseAdj.get(j).add(i)
            if i not in org or j not in org:
                return False
            ingress[j-1] += 1

        # all node should have ingress except the the last ele in org
        if count < (len(org) - 1):
            return False

        #travase org， think as ingress thero, the last element has ingress 0
        for j in org[::-1]:
            print(org, " ", seqs)
            print(ingress)
            print(j)
            if ingress[j - 1]: #the last element indegree should be 0
                return False
            for key in inverseAdj.keys():
                if j in inverseAdj.get(key):
                    inverseAdj.get(key).remove(j) #remove the last element as ingress
                    ingress[key-1] -= 1

        return True            





#Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. 
#The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. 
#Reconstruction means building a shortest common supersequence of the sequences in seqs 
#(i.e., a shortest sequence so that all sequences in seqs are subsequences of it). 
#Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution = Solution()
        self.assertTrue(not solution.sequenceReconstruction([1,2,3], [[1,2],[1,3]]))
        self.assertTrue(not solution.sequenceReconstruction([1,2,3], [[1,2]]))
        self.assertTrue(solution.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]]))
        self.assertTrue(solution.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]))




if __name__ == "__main__" : unittest.main()
