
#include <assert.h>
#include <string.h>


char* newStack(int size) {
    char* stack = (char*)malloc(size + 1);
    strmem(stack, 0, size + 1);
    return stack;
}

void freeStack(char* stack) {
    if (NULL != stack) {
        free(stack);
    }
}

void push(char* stack, char c) {
    int len = strlen(stack);
    stack[len] = c;
}

bool isEmpty(char* stack) {
    return 0 == strlen(stack);
}

char pop(char* stack) {
    int len = strlen(stack);
    char c = stack[len - 1];
    stack[len - 1] = '\0';
    return c;
}

// is () [] {} pairs' right character
bool isRightBracketSymbol(char c) {
    if (c == ')' ||
        c == ']' ||
        c == '}') {
        return true;
    }
    return false;
}

//  get pairs' left character by given character
char getPairedLeftSymbol(char c) {
    if (c == ')') {
        return '(';
    } else if (c == ']') {
        return '[';
    } else if (c == '}') {
        return '{';
    } else {
        return NULL;
    }
}

bool isValid(char* s) {
    int len = strlen(s);
    char* stack = newStack(len)
    for (int i = 0; i < len; i++) {
        if (!isRightBracketSymbol(s[i])) {
            push(stack, s[i]);
        } else if (isEmpty(stack) || pop(stack) != getPairedLeftSymbol(s[i])) {
            return false;
        }
    }
    bool result = isEmpty(stack);
    freeStack(stack);
    return result;
}

void main() {
    assert(isValid("()[]{}"))
    assert(!isValid("(]"))
    assert(!isValid("([)]"))
    assert(isValid("{[]}"))
    assert(!isValid("((("))
}