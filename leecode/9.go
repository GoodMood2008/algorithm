package main

const INT_MAX = int(^uint(0) >> 1)
const INT_MIN = ^INT_MAX

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	input := x
	result := 0
	for input != 0 {
		remNum := input % 10
		if (result > INT_MAX/10) || (result == INT_MAX/10 && remNum > 7) {
			return false
		}
		if (result < INT_MIN/10) || (result == INT_MIN/10 && remNum > 8) {
			return false
		}
		result = 10*result + remNum
		input = input / 10
	}

	return result == x
}

func assert(cond bool) {
    if (!cond) {
        panic("not equal")
    }
}

func main() {
	assert(isPalindrome(121))
	assert(!isPalindrome(-121))
	assert(!isPalindrome(10))
}
