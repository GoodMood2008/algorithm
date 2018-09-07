#include <assert.h>
#include <string.h>

void reverse(char *s, int begin, int end) {
    int i = begin;
    int j = end;
    while (i < j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;
        j--;
    }
}

// ab -> a'b -> a'b' -> ba
void reversestr(char *s, int pos) {
    int len = strlen(s); 
    reverse(s, 0, pos - 1);
    reverse(s, pos, len - 1);
    reverse(s, 0, len - 1);
}

int main() {
    char buf[] = "abcdefgh";
    reversestr(buf, 3);
    assert(0 == strcmp(buf, "defghabc"));  
}