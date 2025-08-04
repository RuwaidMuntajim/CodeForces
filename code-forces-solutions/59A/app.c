#include <stdio.h>
#include <ctype.h>
#include <string.h>



void toUpperCase (char word[]) {
    
    int n;
    for (n = 0; n < strlen(word); n++) {
        toupper(word[n]);
        putchar(word[n]);
    }

    printf("%s", word);
}

void toLowerCase (char word[]) {
    int n;
    for (n = 0; n < strlen(word); n++) {
        tolower(word[n]);
        putchar(word[n]);
    }
    printf("%s", word);
}


int main() {
    char word[] = "";
    int u, l = 0;
    int n;
    
    printf(" ");
    scanf("%s", word);

    for (n = 0; n < strlen(word); n++) {
        if ( isupper(word[n]) ) {
            u += 1;
        } else {
            l += 1;
        }
    }
    if ( u > l ) {
        toUpperCase(word);
    } else {
        toLowerCase(word);
    }
    printf("%s", word);

    return 0;
}