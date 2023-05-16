#include <stddef.h>
#include <stdbool.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head) 
{
    /* Check if the list is empty */
    if (*head == NULL)
    {
        return 1;  /* An empty list is considered a palindrome */
    }

    /* Find the middle node of the list using two-pointer technique */
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;

    while (fast_ptr != NULL && fast_ptr->next != NULL) 
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }

    /* Reverse the second half of the list */
    listint_t *prev = NULL;
    listint_t *current = slow_ptr;
    listint_t *next = NULL;

    while (current != NULL) 
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    /* Compare the reversed second half with the first half of the list */
    listint_t *first_half = *head;
    listint_t *second_half = prev;

    while (second_half != NULL) 
    {
        if (first_half->n != second_half->n) {
            return 0;  /* Not a palindrome */
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;  /* Palindrome */
}

