class Solution:
    def makeSubStr(self, s, i, index):
        result = list()
        if -1 == index:
            result.append(s[i])
            return result
        else:
            index += 1
            while index <= i:
                result.append(s[index])
                index += 1
            return result
            
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict store substring that is not have the same chracter
        subStrLengthList = list()
        tempSubStrList = list()
        for i in range(len(s)):
            c = s[i]
            if c in tempSubStrList:
                subStrLengthList.append(len(tempSubStrList))
                index = s.rfind(c, 0, i)
                tempSubStrList = self.makeSubStr(s, i, index)
            else:
                tempSubStrList.append(c)
        # add last len
        subStrLengthList.append(len(tempSubStrList))
            
        # find the substring which is longest
        return 0 if [] == subStrLengthList else max(subStrLengthList)