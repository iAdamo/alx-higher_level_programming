#include "lists.h"
/**
 * check_cycle - check for cycle singly linked list
 * @list: pointer to head of list
 * Return: 0 if there is no cycle. 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (list == NULL)
		return (0);
	ptr = list->next;
	while (ptr)
	{
		if (ptr->next == list->next)
		{
			return (1);
		}
		else if (ptr->next == NULL)
		{
			return (0);
		}
		ptr = ptr->next;
	}
	return (0);
}
