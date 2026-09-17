#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    char nombre[50];
    int data;
    struct Node* next;
};

struct Node* createNode(const char* nombre, int value) {
    int size = sizeof(struct Node);
    struct Node* newNode = (struct Node*)malloc(size);
    if (newNode == NULL) {
        printf("Error al asignar memoria.\n");
        return NULL;
    }
    strcpy(newNode->nombre, nombre);
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void appendSorted(struct Node** head, const char* nombre, int value) {
    if (*head == NULL || nombre[0] <= (*head)->nombre[0]) {
        struct Node* newNode = createNode(nombre, value);
        newNode->next = *head;
        *head = newNode;
        return;
    }

    struct Node* current = *head;
    while (current->next != NULL && current->next->nombre[0] < nombre[0]) {
        current = current->next;
    }

    struct Node* newNode = createNode(nombre, value);
    newNode->next = current->next;
    current->next = newNode;
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

int main() {
    struct Node* head = NULL;
    char Nombre[50];
    int valor;

    while (1) {
        if (scanf("%49s", Nombre) != 1) break;
        if (strcmp(Nombre, "stop") == 0) break;
        if (scanf("%d", &valor) != 1) break;

        appendSorted(&head, Nombre, valor);
    }

    printList(head);
    return 0;
}