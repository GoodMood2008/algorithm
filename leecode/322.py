#!/user/bin/python
#-*- coding:utf-8 -*-


class Solution:
    # dp[i] 最小步数
    # dp[i] = min([lambda j:dp[i - coins[j]] for range(0, len(conin))])
    # T(n) = O(amount*len(coins))
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, (amount + 1)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        mincoin = min(coins)
        maxcoin = max(coins)
        for i in range(mincoin, (amount + 1)):
            filtercoin = coins if i >= maxcoin else filter(lambda c : c <= i, coins)
            dp[i] = min(map(lambda c : dp[i - c] + 1, filtercoin))
        return dp[amount] if dp[amount] <= amount else -1

    def coinChange3(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minlen = self.dfs3(coins, amount, amount, dict())
        print(minlen)
        return -1 if minlen > amount else minlen
        
    def dfs3(self, coins, amount, curAmount, d):
        print(curAmount, " ", d)
        if curAmount < 0:
            return amount + 1
        elif curAmount == 0:
            return 0
        else:
            temp = []
            for coin in coins:
                if curAmount - coin < 0:
                    continue
                if None == d.get(curAmount - coin):
                    d.update({curAmount - coin : self.dfs3(coins, amount, curAmount - coin, d)})
                temp.append(d.get(curAmount - coin))
            return min(temp) + 1 if temp else (amount + 1)

    def coinChange4(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        minlen = self.dfs(coins, amount, amount)
        return -1 if minlen > amount else minlen
        
    def dfs4(self, coins, amount, curAmount):
        if curAmount < 0:
            return amount + 1
        elif curAmount == 0:
            return 0
        else:
            temp = []
            for coin in coins:
                temp.append(self.dfs(coins, amount, curAmount - coin))
            return min(temp) + 1      

#You are given coins of different denominations and a total amount of money amount. 
#Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
import unittest
class SolutionTestCase(unittest.TestCase):
    def testCaseSolution(self): 
        solution = Solution()
        self.assertTrue(solution.coinChange([1, 2, 5], 11) == 3)
        self.assertTrue(solution.coinChange([2], 3) == -1)
        self.assertTrue(solution.coinChange([370,417,408,156,143,434,168,83,177,280,117], 9953) == 24)

if __name__ == "__main__" : unittest.main()