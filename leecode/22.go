package main

import "fmt"

func generateParenthesis(n int) []string {
	results := make([]string, 0)
	backtrack(&results, "", 0, 0, n)
	return results
}

func backtrack(results *[]string, result string, left int, right int, num int) {
	if (left + right) == num*2 {
		*results = append(*results, result)
	}
	if left < num {
		backtrack(results, result+"(", left+1, right, num)
	}
	if right < left {
		backtrack(results, result+")", left, right+1, num)
	}
}

func assert(cond bool) {
	if !cond {
		panic("not equal")
	}
}

func main() {
	results := generateParenthesis(3)
	for _, item := range results {
		fmt.Println(item)
	}
}
