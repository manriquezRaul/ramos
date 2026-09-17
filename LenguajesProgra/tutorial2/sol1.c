#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr1, *ptr2;
    ptr1 = (int *)malloc(sizeof(int));
    if (ptr1 == NULL) {
        printf("Memoria insuficiente\n");
        return -1;
    }
    *ptr1= 10;
    ptr2= ptr1;
    printf("Valor de ptr2: %d\n", *ptr2);
    *ptr1=40;
     printf("Valor de ptr2: %d\n", *ptr2);
    free(ptr1);

}

