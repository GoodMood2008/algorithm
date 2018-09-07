
#include <limits.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#include <stdio.h>

int myAtoi(char* str) {
    int len = strlen(str);
    int pos = 0;

    // skip white
    for ( ; isspace(str[pos]); pos++);

    // first char is '-', it negtive
    int symbol = ('-' == str[pos]) ? -1 : 1;

    if ('+' == str[pos] || '-' == str[pos]) {
        pos++;
    }

    int result = 0;
    // calc until end
    while (isdigit(str[pos])) {
        int inputDigit = (str[pos++] - '0');
        if ((result > INT_MAX / 10) || (result == INT_MAX / 10 && inputDigit > 7)) return INT_MAX;
        if ((result < INT_MIN / 10) || (result == INT_MIN / 10 && inputDigit > 8)) return INT_MIN;
        result = result * 10 + inputDigit * symbol;
    }

    return result;
}



void main() {
    assert(myAtoi("") == 0);
    assert(myAtoi("   ") == 0);
    assert(myAtoi(" -abc") == 0);
    assert(myAtoi(" -") == 0);
    assert(myAtoi("42") == 42);
    assert(myAtoi("-42") == -42);
    assert(myAtoi(" 4193 with word") == 4193);
    assert(myAtoi("word with 987") == 0);
    assert(myAtoi("-91283472332") == -2147483648);
    assert(myAtoi("91283472332") == 2147483647);
}