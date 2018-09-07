
#include <limits.h>
#include <assert.h>

int reverse(int x) {
    int result = 0;
    int pop = 0;
    while (x != 0) {
        pop = x % 10;
        x = x / 10;
        if ((result > INT_MAX / 10) || (result == INT_MAX / 10 && pop > 7)) return 0;
        if ((result < INT_MIN / 10) || (result == INT_MIN / 10 && pop < -8)) return 0;
        result = result * 10 + pop;
    }

    return result;
}

void main() {
    assert(reverse(123) == 321);
    assert(reverse(-123) == -321);
    assert(reverse(1534236469) == 0);

}