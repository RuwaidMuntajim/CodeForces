// take in num of chars
// take string of chars
// compare nth char with (n+1)th char
#include <stdio.h>
int main () {
    int num = 0;
    int n;
    int j = 0;
    
    printf(" ");
    scanf("%d", &num);
    char stone[num];
    printf(" ");
    scanf("%s", stone);
    for (n = 0; n < num; n++) {
        if (stone[n] == stone[n+1]) {
            j = j + 1;
        }
    }
    printf("%d\n", j);
    return 0;
}