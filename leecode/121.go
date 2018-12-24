package main

func max(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func min(a int, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}


func maxProfit(prices []int) int {
    if len(prices) == 0{
        return 0
    }
    maxPorf, minPri := 0, prices[0]
    for _, price := range prices[1:] {
        if price < minPri {
            minPri = price
        } else {
            maxPorf = max(maxPorf, price - minPri)
        }
    }
    return maxPorf
}

func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

//Say you have an array for which the ith element is the price of a given stock on day i.
//If you were only permitted to complete at most one transaction 
//(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
//Note that you cannot sell a stock before you buy one.
func main() {
    input := [6]int{7,1,5,3,6,4}
    assert(maxProfit(input[:]) == 5)       
}