#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <malloc.h>

struct str
{
    char *s;
    int pos;
};

char *mallocChar(int len) {
    char *s = (char*)malloc(len + 1);
    memset(s, 0, len + 1);
    return s;
}

struct str *mallocStr(int numRows, int charLen) {
    struct str *strArray = (struct str *)calloc(numRows, sizeof(struct str));
    for (int i = 0; i < numRows; i++) {
        strArray[i].s = mallocChar(charLen);
        strArray[i].pos = 0;
    }    
    return strArray;
}

void freeStr(struct str *strArray, int numRows) {
    for (int i = 0; i < numRows; i++) {
        free(strArray[i].s);
    }
    free(strArray);    
}

void printStr(struct str *array, int numRows) {
    for (int i = 0; i < numRows; i++) {
        printf("elem[%d] : %s %d, ", i, array[i].s, array[i].pos);
    }
    printf("\n");
}


char* convert(char* s, int numRows) {
    if (numRows == 1) {
        return s;
    }
    
    int len = strlen(s);

    struct str *strArray = mallocStr(numRows, len);

    int strPos = 0;
    int direction = 1;
    for (int i = 0; i < len; i++) {
        strArray[strPos].s[strArray[strPos].pos++] = s[i];
        if (0 != i && (strPos == 0 || strPos == numRows - 1)) {
            direction = 0 - direction;
        } 
        strPos += direction;
    }

    char *result = mallocChar(len);
    for (int i = 0; i < numRows; i++) {
        strcat(result, strArray[i].s);
    }


    freeStr(strArray, numRows);

    return result;
 }


int main() {
    assert(!strcmp(convert("abcde", 2), "acebd"));
    assert(!strcmp(convert("abcde", 3), "aebdc"));  
    return 0;  
}