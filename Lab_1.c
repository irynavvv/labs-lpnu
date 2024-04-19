#include <stdio.h>

int main() {
    int n, i, s;
    s = 0;
    printf("Please enter value for N\n");
    scanf("%d", &n);
    for (i = 1; i < n; i++) {
        if (i % 2 == 0) {
            s = s + i;
            printf("Current value i=%d S=%d\n", i, s);
        }
    }
    printf("Final result sum is S=%d\n", s);
    return 0;
}
