#include <assert.h>
#include <string.h>
#include <stdlib.h>

int MAX_SIZE = 1024;
char buf[1024];
int pos = 0;

char* alloc(int size) {
    if (pos + size < MAX_SIZE) {
        int temp = pos;
        pos += size;
        return buf + temp;
    }
    return NULL;
}

// 递归中如果碰到要分配内存非常麻烦，遇到这种情况有时alloc可以帮上忙
char* longestCommonPrefix(char** strs, int strsSize) {
    if (0 == strsSize) {
        return "";
    }
    if (1 == strsSize) {
        return strs[0];
    }

    char* comPrefix1 = longestCommonPrefix(strs, strsSize/2);
    char* comPrefix2 = longestCommonPrefix(strs + strsSize/2, strsSize - strsSize/2);
    
    int len1 = strlen(comPrefix1);
    int len2 = strlen(comPrefix2);
    // if one of comPrefix is empty, return ""
    if (len1 == 0 || len2 == 0) {
        return "";
    }

    // get the small length of length
    int minLen = len1 > len2 ? len1 : len2;
    // malloc space
    char * result = (char*)alloc(minLen + 1);

    // compare
    int i = 0;
    while (i < minLen) {
        if (comPrefix1[i] != comPrefix2[i]) {
            break;
        }
        result[i] = comPrefix1[i];
        i++;
    }

    // return result
    return result;
}



void main() {
    char* input1[3] = {"flower","flow","flight"};
    assert(!strcmp(longestCommonPrefix(input1, 3), "fl"));
    char* input2[3] = {"dog","racecar","car"};
    assert(!strcmp(longestCommonPrefix(input2, 3), ""));
}