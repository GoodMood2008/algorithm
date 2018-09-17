
#include <limits.h>
#include <assert.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    int input = x;
    int result = 0;
    while (input != 0) {
        int remNum = input % 10;
        if ((result > INT_MAX / 10) || (result == INT_MAX / 10 && remNum > 7)) return false;
        if ((result < INT_MIN / 10) || (result == INT_MIN / 10 && remNum > 8)) return false;
        result = 10 * result + remNum;
        input = input / 10;
    }

    return result == x;
}

void main() {
    assert(isPalindrome(121));
    assert(!isPalindrome(-121));
    assert(!isPalindrome(10));
}