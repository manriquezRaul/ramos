#include <stdio.h>
#include <stdlib.h>

// Define the Node struct
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
// Print the linked list
void printList(Node* node) {
    while (node) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("null\n");
}

void append(struct Node** head_ref, int new_data) {
    Node* new_node = createNode(new_data);
    Node* last = *head_ref;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        new_data= new_data * 2;
        for (int i ; i < 500; i++) {
      (*head_ref)->data = (*head_ref)->data * new_data;
   }
        return;
    }
    else append(&((*head_ref)->next), new_data);
}

int main() {
    // Explicitly creating and connecting nodes
    Node* node1 = createNode(3);
    Node* node2 = createNode(5);

    printList(node1);

    // Free the memory
    free(node1);

    return 0;
  }