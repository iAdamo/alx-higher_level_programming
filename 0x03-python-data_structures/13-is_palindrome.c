#include "lists.h"






int is_palindrome(listint_t **head)
{
	listint_t *len, *temp;
	size_t count = 0, i = 0, flag = 0, idx;

	len = *head;
	temp = *head;
	if (*head == NULL)
		return (1);
	while (len->next)
	{
		count++;
		len = len->next;
	}
	ptr = malloc(sizeof(int) * count);
	if (ptr == NULL)
		return (NULL);
	while (temp->next)
	{
		ptr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	i = 0;
	idx = count - 1;
	while (i < count / 2)
	{
		if (ptr[i] == ptr[idx])
			flag = 1;
		i++;
		idx--;
	}
	free(ptr);
	if (flag == 1)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
