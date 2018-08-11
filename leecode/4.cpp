#include <malloc.h>
#include <stdio.h>
#include <time.h>

double findMedian(int *numCombine, int numSize) {
    if (numSize % 2 == 0) {
        return (double)((numCombine[numSize/2 - 1] + numCombine[numSize/2])) / 2; 
    } else {
        return (double)numCombine[numSize/2];
    }

}

void copyRemainArray(int* numCombine, int pos, int* nums, int posNum, int numSize) {
    if (posNum >= numSize) {
        return;
    }

    for (int i = posNum; i < numSize; ++i) {
        *(numCombine + pos++) = *(nums + i);
    }

}

void reorderTwoArray(int* numCombine, int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0;
    int j = 0;
    int c = 0;
    // 使用i和j轮流拷贝数据到目标中，直至有一个数组已经访问结束
    while (!(i == nums1Size || j == nums2Size)) {
        if (*(nums1 + i) < *(nums2 + j)) {
            *(numCombine + c++) = *(nums1 + i);
            i++;
        } else {
            *(numCombine + c++) = *(nums2 + j);
            j++;            
        }
    }

    // 拷贝剩下的那个数组剩余的值
    copyRemainArray(numCombine, c, nums1, i, nums1Size);
    copyRemainArray(numCombine, c, nums2, j, nums2Size);
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* numCombine = (int*)calloc(nums1Size + nums2Size, sizeof(int)); // assigned space to store result
    reorderTwoArray(numCombine, nums1, nums1Size, nums2, nums2Size);
    double median = findMedian(numCombine, nums1Size + nums2Size);
    free(numCombine);
    return median;
}

int main(int argc, char* argv[]) {
    int array1[3] = {1, 2, 5};
    int array2[2] = {3, 4};
    long t1 = clock();
    time_t time1;
    time(&time1);
    double median = findMedianSortedArrays(array1, 3, array2, 2);
    time_t time2;
    time(&time2);
    printf("the time is %f\n", difftime(time2, time1));
    long t2 = clock();
    printf("the time is %f\n",  t2 - t1);
    printf("%f", median);
    return 0;
}