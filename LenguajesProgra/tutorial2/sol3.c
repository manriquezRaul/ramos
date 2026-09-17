#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* createNode(int value) {
    struct Node* newNode ;
    int size = sizeof(struct Node);
    newNode = (struct Node*)malloc(size);
    if (newNode == NULL) {
        printf("Error al asignar memoria\n");
        return  NULL;
    }
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}
void append(struct Node** head, int value) {
    struct Node* newNode = createNode(value);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    else {
         append(&((*head)->next), value);
    }
}
void printList(struct Node* head) {
    if (head != NULL) {
        printf("%d -> ", head->data);
        printList(head->next);
    }
    else {
        printf("NULL\n");
    }
}
int main() {
    struct Node* head = NULL;
    append(&head, 10);
    append(&head, 20);
    append(&head, 30);
    printList(head);
    return 0;
}