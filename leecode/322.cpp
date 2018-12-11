#include <assert.h>
#include <malloc.h>
#include <stdio.h>
int min(int i, int j) {
    if (i > j) {
        return j;
    } else {
        return i;
    }
}

int coinChange(int* coins, int coinsSize, int amount) {
    // init dp array
    int* dp = (int*)malloc((amount + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i < amount + 1; ++i) {
        dp[i] = amount + 1;
    }

    // use dp 
    for (int i = 1; i <= amount; ++i) {
        for (int j = 0; j < coinsSize; ++j) {
            if (i >= coins[j]) {
                // dp i is equal to the minimum dp[i - coins[j]] + 1
                dp[i] = min(dp[i], dp[i - coins[j]]  + 1);
            }
        }
    }

    int result = dp[amount];
    // free dp array, this is argly
    free(dp);
    return result > amount ? -1 : result;
}



//You are given coins of different denominations and a total amount of money amount. 
//Write a function to compute the fewest number of coins that you need to make up that amount. 
//If that amount of money cannot be made up by any combination of the coins, return -1.
void main() {
    int input1[3] = {1, 2, 5};
    assert(coinChange(input1, 3, 11) == 3);
    int input2[1] = {2};
    assert(coinChange(input2, 1, 3) == -1);
    int input3[11] = {370,417,408,156,143,434,168,83,177,280,117};
    assert(coinChange(input3, 11, 9953) == 24);
    int input4[1] = {1};
    assert(coinChange(input4, 1, 1) == 1);
}