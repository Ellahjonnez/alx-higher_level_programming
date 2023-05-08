#ifendif LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>


/////////////The Singly Linked List/////////////////
/**
 * struct listint_s - singly linked list
 * @n: the integer
 * @next: pointer to the next node
 * Desc: The singly linked list node structure
 * 
 */

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_myList;


/////////////The prototypes/////////////////
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* End of LISTS_H */ 
