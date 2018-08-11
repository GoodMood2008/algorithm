
#include <stdio.h>
#include <string.h>

// 判断i 到 j -1 是否存在字符s[j]
int hasChar(char* s, int i, int j) {
    if (j <= i) {
        return 0;
    }
    char c = s[j];
    for (int pos = i; pos < j; pos++) {
        if (s[pos] == c) {
            return pos + 1;
        }
    }
    return 0;
}

int max(int i, int j) {
    return i > j ? i : j;
}

int lengthOfLongestSubstring(char* s) {
    int i = 0;
    int length = strlen(s);
    int maxlength = 0;
    int j = 0;
    for (; j < length; j++) {
        int pos = hasChar(s, i, j);
        if (pos) {
            maxlength = max(j - i, maxlength);             // 更新最大长度
            i = pos;                                       // 滑动窗口新i
        }
    }
    maxlength = max(j - i, maxlength); // 只有一个元素特殊情况
    return maxlength;
}

int main(int argc, char* argv[])
{
    char *s0 = "abcabcbc";
    printf("%d\n", lengthOfLongestSubstring(s0));
    char *s1 = "bbbbbbb";
    printf("%d\n", lengthOfLongestSubstring(s1));
    char *s2 = "awkwk";
    printf("%d\n", lengthOfLongestSubstring(s2));    
    return 0;
}