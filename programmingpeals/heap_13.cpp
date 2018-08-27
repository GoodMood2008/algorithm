#include <stdio.h>
#include <string.h>
#include <assert.h>

int array[100];
int length = 1;

void printArray() {
    for (int i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// level1
int value(int pos) {
    assert(pos < 100);
    return array[pos];
}

void setValue(int pos, int value) {
    array[pos] = value;
}

int leftChild(int i) {
    return 2 * i;
}

int rightChild(int i) {
    return 2 * i + 1;
}

int parent(int i) {
    return i / 2;
}

void switchValue(int pos1, int pos2);

// level2
void shiftUp(int n) {
    // i
    int pos = n - 1;
    while (true) {
        if (pos == 1) {
            break;
        }
        int parentId = parent(pos);
        if (value(pos) < value(parentId)) {
            switchValue(pos, parentId);
        }
        pos = parentId;
    }
    
}

void switchValue(int pos1, int pos2) {
    int temp = value(pos1);
    setValue(pos1, value(pos2));
    setValue(pos2, temp);
}


// 把首节点往下调整
void shiftDown(int n) {
    int i = 1;
    while (true) {
        int c = 2 * i;
        if (c > n) { // 没有可以调整的
            break;
        }
        // 取左右节点较小的节点
        if (c + 1 <= n) {
            if (value(c + 1) < value(c)) {
                c++;
            }
        }

        // 比父节点大，则不用调整
        if (value(c) > value(i)) {
            break;
        }

        // 交互数值
        switchValue(c, i);

        // 移动新点
        i = c;
    }
}

// level2 priorityQueue
void insert(int i) {
    if (length >= 100) {
        printf("array is full, you can't put any more element\n");
        return;
    }

    // 设置最后一个元素为i
    length++;
    setValue(length - 1, i);
    // level2层操作
    shiftUp(length);

}

int extractmin() {
    if (length < 1) {
        printf("array is empty, you can't extract any more element\n");
        return -1;
    }
    int result = value(1);
    setValue(1, value(--length));
    shiftDown(length);
    return result;
}


// level3 order
void heapOrder(int *s, int size) {
    for (int i = 0; i < 10; i++) {
        insert(s[i]);
    }
    for (int i = 0; i < 10; i++) {
        s[i] = extractmin();
    }    
}

void printSource(int *s, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", s[i]);
    }
}
// level4 排序
int main() {
    memset(array, 0, 100);
    int s[10] = {1, 3, 2, 5, 8, 9, 10, 6, 4, 7};
    heapOrder(s, 10);
    printSource(s, 10);
    return 0;
}
