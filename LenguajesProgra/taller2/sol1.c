#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    char nombre[50];
    int data;
    struct Node* next;
};
 struct Node lista[50];

struct Node* createNode(int value , const char * nombre1) {
    struct Node* newNode ;
    int size = sizeof(struct Node);
    newNode = (struct Node*)malloc(size);
    if (newNode == NULL) {
        printf("Error al asignar memoria\n");
        return  NULL;
    }
    newNode->data = value;
    strcpy(newNode->nombre, nombre1);
    newNode->next = NULL;
    return newNode;
}

void printList(struct Node* head) {
    int i = 0;
    while (head != NULL) {
        printf("- Nodo %d\n", ++i);
        printf("%s, %d\n", head->nombre, head->data);
        printf("- - - - - - ");
        printf("\n");
        head = head->next;
    }
}

void printInverse(struct Node* head, int* i) {
    if (head == NULL) {
        return;
    }

    printInverse(head->next, i);
    printf("- Nodo %d\n", ++(*i));
    printf("%s, %d\n", head->nombre, head->data);
    printf("- - - - - - \n");
}

int main() {
    struct Node* head = NULL;
    int cantidad = 0;
    for (int i = 0; i < sizeof(lista) / sizeof(lista[0]); i++) {
        scanf("%49s", lista[i].nombre);
        if (strcmp(lista[i].nombre, "stop") == 0) {
            break; }
        scanf("%d", &lista[i].data);
        lista[i].next = NULL;
        if (i > 0) {
            lista[i - 1].next = &lista[i];
        }
        cantidad++;
    }

    if (cantidad > 0) {
        head = &lista[0];
    }
    int posicion = 0;
    printInverse(head, &posicion);
    return 0;
}