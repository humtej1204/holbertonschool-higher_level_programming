#include "lists.h"
/**
 * comparator - compare start and end position
 * @head: the linked list
 * @last: the end of the list
 * Return: 1 true, 0 false
 */
int comparator(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (comparator(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the linked list
 * Return: 1 true, 0 false
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (comparator(head, *head));
}
