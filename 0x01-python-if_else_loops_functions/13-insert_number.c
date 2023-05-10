#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head list
 * @number: the number to store in the new node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new;
        listint_t *top;

        top = *head;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        while (top->next != NULL)
        {
                if ((top->next)->n >= number)
                {
                        new->next = top->next;
                        top->next = new;
                        return (new);
                }
                top = top->next;
        }

        new->next = NULL;
        top->next = new;
        return (new);
}
