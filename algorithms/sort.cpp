#include <stdio.h>



void print(int* a, int n);

void bubbleSort(int* a, int n) {
    if (n == 0 || n == 1){
        return;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++){
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
         }
     }
}

void insertSort(int* a, int n) {
    if (n == 0 || n == 1) {
        return;
    }
    for (int i = 1; i < n; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (a[j+1] < a[j]) {
                int temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
         }
    }
}

void print(int* a, int n) {
    printf("{");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("}\n");
}

int main() {
    int a[5] = {5, 4, 3, 2, 1};
    print(a, 5);
    bubbleSort(a, 5);
    print(a, 5);
    printf("insert sort");
    int b[5] = {5, 4, 3, 2, 1};
    insertSort(b, 5);
    print(b, 5);
}
