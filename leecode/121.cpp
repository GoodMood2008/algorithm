#include <assert.h>


int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) {
        return 0;
    }    
    int minPrice = prices[0];
    int maxProf = 0;
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        } else {
            maxProf = prices[i] - minPrice ? prices[i] - minPrice > maxProf : maxProf;
        }
    }
    return maxProf;
}


//Say you have an array for which the ith element is the price of a given stock on day i.
//If you were only permitted to complete at most one transaction 
//(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
//Note that you cannot sell a stock before you buy one.
void main() {
    int input[6] = {7,1,5,3,6,4};
    assert(maxProfit(input, 6) == 5);
}