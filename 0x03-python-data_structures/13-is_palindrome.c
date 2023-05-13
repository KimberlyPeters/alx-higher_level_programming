#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the first element on the list
 *
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int list_len = 0, i = 0, middle, *list;
	listint_t *curr;

	if (*head == NULL)
		return (1);

	curr = *head;

	while (curr)
	{
		list_len++;
		curr = curr->next;
	}
	curr = *head, list = malloc(sizeof(int) * list_len);
	while (curr)
	{
		list[i] = curr->n;
		i++;
		curr = curr->next;
	}

	middle = list_len / 2;
	i = 0;
	while (i < middle)
	{
		if (list[i] == list[list_len - 1])
		{
			i++;
			list_len--;
		}
		else
			return (0);
	}
	free(list);
	return (1);
}
