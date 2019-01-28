#include <assert.h>
#include <malloc.h>

int numTrees(int n) {
    if (n < 2) {
        return n;
    }

    int *array = (int*)malloc((n + 1)*sizeof(int));
    for (int i = 0; i < n + 1; i++) {
        array[i] = 0;
    }

    array[0] = array[1] = 1;
    for (int i = 2; i < n + 1; i++) {
        for (int j = 0; j < i; j++) {
            array[i] += array[j] * array[i - j - 1];
        }
    }

    int result = array[n];

    free(array);
    return result;
}

void main() {
    assert(numTrees(3) == 5);
}