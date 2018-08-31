#zigzag串
class Solution:
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (1 == numRows):
            return s
        result = list()
        maxLength = len(s)
        for i in range(numRows):
            j = 0
            pos = i
            while pos < maxLength:
                result.append(s[pos])
                pos = pos + 2 * (numRows - 1 - i)
                if (pos < maxLength) and (i != 0) and (i != numRows - 1):
                    result.append(s[pos])
                j += 1 
                pos = (numRows - 1) * 2 * j + i
        return "".join(result)

    # 横向扫描,按行存储，可以计算出该数据属于哪一行，存在对应的行中
    # 用数组位置和方向的思路，整个算法简洁明了
    def convert(self, s, numRows):
        import functools
        if (1 == numRows):
            return s

        result = list()
        for i in range(numRows):
            result.append([])

        direction = 1
        pos = 0
        for i in range(len(s)):
            result[pos].append(s[i])
            if (i !=0 and (pos == 0 or (pos == (numRows - 1)))):
                direction = 0 - direction
            pos += direction

        return "".join(functools.reduce(lambda x, y : x + y, result, []))


import unittest
class SolutionTestCase(unittest.TestCase):
    def testZigzag(self):
        solution = Solution()
        self.assertEqual(solution.convert("abcde", 2), "acebd")
        self.assertEqual(solution.convert("abcde", 3), "aebdc")

if __name__ == "__main__": unittest.main()

