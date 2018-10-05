#/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mapNegative = dict()
        negatives = list()
        mapPositive = dict()
        postives = list()
        zeros = list()

        # put nums to maps
        for i in nums:
            if 0 == i:
                zeros.append(i)
            elif i > 0:
                mapPositive[i] = 0
                postives.append(i)
            else:
                mapNegative[i] = 0
                negatives.append(i)

        result = list()        
        
        # if has 0, than traversing the negatives
        if len(zeros) > 0:
            for i in mapNegative.keys():
                pos = 0 - i
                if None != mapPositive.get(pos):
                    result.append([i, 0, pos])
        
        # if has more than three zero, add [0, 0, 0] to result
        if len(zeros) >= 3:
            result.append([0, 0, 0])

        # than traversing the negative two sums,if
        # the negative of tow sums is contain in postives
        # than add to result
        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                n1 = negatives[i]
                n2 = negatives[j]
                pos = 0 - (n1 + n2)
                if None != mapPositive.get(pos):
                    n1, n2 = (n2, n1) if n1 > n2 else (n1, n2)
                    result.append([n1, n2, pos])

        # than traversing the positive of two sums,if
        # the negative of two sums is contain in negtives
        # than add to result
        for i in range(len(postives)):
            for j in range(i + 1, len(postives)):
                p1 = postives[i]
                p2 = postives[j]
                neg = 0 - (p1 + p2)
                if None != mapNegative.get(neg):
                    p1, p2 = (p2, p1) if p1 > p2 else (p1, p2)
                    result.append([neg, p1, p2])

        nonRepeativeResult = list()
        for i in result:
            if nonRepeativeResult.count(i) == 0:
                nonRepeativeResult.append(i)            
        return nonRepeativeResult


    def orderList(self, negV, posV, value):
        if value < 0:
            negV, value = (value, negV) if (negV > value) else (negV, value)
            return [negV, value, posV]
        else:
            posV, value = (value, posV) if posV > value else (posV, value)
            return [negV, posV, value]

    def threeSum(self, nums):
        numdict = {}
        result = []
        for i in nums:
            numdict[i] = numdict.get(i, 0) + 1
        if numdict.get(0, 0) >= 3:
            result.append([0, 0, 0])

        neg = list(filter(lambda x : x <= 0, numdict))
        pos = list(filter(lambda x : x > 0, numdict))

        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in numdict:
                    if dif in (i, j) and numdict.get(dif, 0) >= 2:
                        result.append(self.orderList(i, j, dif))
                    if dif < i or dif > j:
                        result.append(self.orderList(i, j, dif))

        print(result)
        return result





import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self):
        solution = Solution()
        self.assertTrue(solution.threeSum([-1, 0, 1, 2, -1, 4]) == [[-1, 0, 1], [-1, -1, 2]])
        self.assertTrue(solution.threeSum([0, 0, 0]) == [[0, 0, 0]])

if __name__ == "__main__" : unittest.main()