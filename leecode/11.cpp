#include <assert.h>


int min(int i, int j) {
    return i < j ? i : j;
}

int max(int i, int j) {
    return i > j ? i : j;
}

// Note: You may not slant the container and n is at least 2.
// the direct method
int maxArea(int* height, int heightSize) {
    int area = 0;
    for (int i = 0; i < heightSize; i++) {
        for (int j = i + 1; j < heightSize; j++) {
            int temp = (j - i) * min(height[i], height[j]);
            area = max(area, temp);
        }
    }    
    return area;
}

int maxArea1(int* height, int heightSize) {
    int area = 0;
    int l = 0; 
    int r = heightSize - 1;
    while (l < r) {
        int temp = (r - l) * min(height[l], height[r]);
        area = max(area, temp);
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }
    return area;
}


void main() {
    int input[9] = {1,8,6,2,5,4,8,3,7};
    assert(maxArea(input, 9) == 49);
    assert(maxArea1(input, 9) == 49);
}