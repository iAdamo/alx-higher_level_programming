#include "lists.h"
/**
 * check_cycle - check for cycle singly linked list
 * @list: pointer to head of list
 * Return: 0 if there is no cycle. 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;
	while (ptr && ptr->next)
	{
		ptr = ptr->next;
		if (ptr->next == list)
			return (1);
	}
	return (0);
}
