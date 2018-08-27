

// 位向量操作，实际是使用数组作为空间，操作数组的位，需要用到| & ~几个操作符

#define SHIFT 5 // 32 = 2^5
#define MASK 0x1F

// i>> SHIFT相当于i/32，将i定位到哪个int
// i&MASK相当于i%MASK，定位i在int中第几位


void set(int i) {
    a[i>>SHIFT] |= (1<<(1&MASK));
}

void clr(int i) {
    a[i>>SHIFT] &= ~(1<<(i&MASK));
}

int test(int i) {
    return a[i>>SHIFT] & (1<<(i&MASK));
}