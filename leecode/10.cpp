
#include <assert.h>
#include <string.h>


// s is lower a - z
// p is lower a - z or '.' or '*'
// '.' represent any a-z
// '*' represent 0..N previous charactor
bool isMatch(char* s, char* p) {
    int sLen = strLen(s);
    int sPat = strLen(p);
    if (0 == sPat) {
        return 0 == sLen;
    }

    bool firstMatch = 0 != sLen && (p[0] == '.' || p[0] == s[0]);
    if ((sPat > 1) && (p[1] == '*')) {
        return firstMatch && isMatch(s + 1, p) || isMatch(s, p + 2);
    } else {
        return firstMatch && isMatch(s + 1, p + 1);
    }
}



void main() {
    assert(!isMatch("ab", ".*c"));
    assert(!isMatch("", "a"));
    assert(!isMatch("aa", "a"));
    assert(isMatch("aa", "a*"));
    assert(isMatch("ab", ".*"));
    assert(isMatch("ab", ".*"));
    assert(isMatch("aab", "c*a*b"));
    assert(!isMatch("mississippi", "mis*is*p*."));
    assert(isMatch("aaa", "a*a"));
    assert(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"));
    assert(isMatch("aaa", "ab*a*c*a"));
    assert(isMatch("aaab", "ab*a*c*ab"));
    assert(isMatch("aaab", ".*.."));
}