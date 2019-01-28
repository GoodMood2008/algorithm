package main

func numTrees(n int) int {
    if n < 2 {
        return n
    }
    result := make([]int, n + 1)
    result[0] = 1
    result[1] = 1

    for i:= 2; i < n + 1; i++ {
        for j:= 0; j < i; j++ {
            result[i] += result[j] * result[i - j - 1]
        }
    }

    return result[n]
}


func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

func main() {
    assert(numTrees(3) ==  5)
}