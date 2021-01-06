#include <stdio.h>

int key = 12;
int a = 1;
int b = 1;

int main(){
    if (key % 2 == 0){
        if (a == 1){
            printf("key mod 2 == 0 and a == 1");
        } else {
            printf("key mod 2 == 0 and a != 1");
        }
    } else {
        if (b == 1){
            printf("key mod 2 != 0 and b == 1");
        } else {
            printf("key mod 2 != 0 and b != 1");
        }
    }
    return 0;
}
