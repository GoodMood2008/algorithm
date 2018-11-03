#include <assert.h>
#include <malloc.h>
#include <string.h>

struct stack {
    int* values;
    int top;
};

stack* makeStack(int len) {
    stack* st = (stack*)malloc(sizeof(stack));
    st->values = (int*)malloc(len*sizeof(int));
    st->top = -1;
    return st;
}

void releaseStack(stack* st) {
    if (NULL != st->values) {
        free(st->values);
    }
    free(st);
}

void put(stack* st, int i) {
    st->top++;
    st->values[st->top] = i;
}

int pop(stack* st) {
    assert(st->top != -1);
    int result = st->values[st->top];
    st->top--;
    return result;
}

int peek(stack* st) {
    assert(st->top != -1);
    return st->values[st->top];
}

bool empty(stack* st) {
    return st->top == -1;
}

int max(int i, int j) {
    if (i < j) {
        return j;
    } else {
        return i;
    }
}

int longestValidParentheses(char* s) {
    int len = strlen(s);
    stack* st = makeStack(len);
    put(st, -1);
    int maxlen = 0;
    for (int i = 0; i < len; i++) {
        if ('(' == s[i]) {
            put(st, i);
        } else {
            pop(st);
            if (empty(st)) {
                put(st, i);
            } else {
                int top = peek(st);
                maxlen = max(maxlen, i - top);
            }
        }
    }
    return maxlen;
}

void main() {
    assert(longestValidParentheses("((") == 0);
    assert(longestValidParentheses("(()") == 2);
    assert(longestValidParentheses("(())()") == 6);    
}