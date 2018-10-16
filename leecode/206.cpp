#include <assert.h>
#include <malloc.h>
#include <stdio.h>

 struct ListNode {
     int val;
     struct ListNode *next;
 };

struct ListNode* reverseList(struct ListNode* head) {
    ListNode* cur = head;
    ListNode* prev = NULL;
    while (cur != NULL) {
        ListNode* temp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = temp;
    }
    return prev;
}

ListNode* newNode(int i) {
    ListNode* result = (ListNode*)malloc(sizeof(ListNode));
    result->val = i;
    result->next = NULL;
    return result;
}

void freeNode(ListNode* node) {
    if (node != NULL) {
        node->next = NULL;
        free(node);        
    }
}

// 使用了sentinail，指针写代码很容易出错
ListNode* convertToList(int* input, int n) {
    ListNode* centinail = newNode(-1);
    ListNode* cur = centinail;
    for (int i = 0; i < n; i++) {
        ListNode* node = newNode(input[i]);
        cur->next = node;
        cur = cur->next;
    }
    ListNode* result = centinail->next;
    freeNode(centinail);
    return result;
}

void print(ListNode* node) {
    ListNode* cur = node;
    while (cur != NULL) {
        printf("%d ", cur->val);
        cur = cur->next;
    }
    printf("\n");
}

void main() {
    int input[5] = {1, 2, 3, 4, 5};
    int output[5] = {5, 4, 3, 2, 1};
    ListNode* head = convertToList(input, 5);
    print(head);
    ListNode* result = reverseList(head);
    ListNode* cur = result;
    int pos = 0;
    while (cur != NULL) {
        printf("%d ", cur->val);
        assert(cur->val == output[pos]);
        cur = cur->next;
        pos += 1;
    }
}