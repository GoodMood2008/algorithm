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

void exchange(int* a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;    
}

int patition(int*a, int p, int q) {
    int x = a[p];
    int i = p;
    for (int j = p + 1; j <= q; j++) {
        if (a[j] < x) {
            i++;
            exchange(a, i, j);
        }
    }
    exchange(a, p, i);
    return i;
}

void quickSort(int* a, int p, int q) {
    if (p < q) {
        int  i = patition(a, p, q);
        quickSort(a, p, i - 1);
        quickSort(a, i + 1, q);
    }
}

void quickSort(int* a, int n) {
    if (n == 0 || n == 1) {
        return;
    }
    quickSort(a, 0, n - 1);
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
    int c[5] = {5, 4, 3, 2, 1};
    quickSort(c, 5);
    print(c, 5);
}
