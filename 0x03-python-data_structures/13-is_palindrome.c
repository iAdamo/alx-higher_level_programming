#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to first node
 * Return:  0 if it is not a palindrome, 1 if it is a palindrome
 * an empty list is considered a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *len, *temp;
	size_t count = 0, i = 0, idx;
	int ptr[2048];

	len = *head;
	temp = *head;
	if (*head == NULL)
		return (1);
	while (len)
	{
		count++;
		len = len->next;
	}
	while (temp)
	{
		ptr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	i = 0;
	idx = count - 1;
	while (i < count / 2)
	{
		if (ptr[i] != ptr[idx])
			return (0);
		i++;
		idx--;
	}
	return (1);
}
