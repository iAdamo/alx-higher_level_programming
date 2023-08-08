#include "lists.h"
/**
 * check_cycle - check for cycle singly linked list
 * @list: pointer to head of list
 * Return: 0 if there is no cycle. 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptrs;

	ptr = ptrs = list;
	while (ptr && ptrs, ptr->next, ptrs->next)
	{
		ptr = ptr->next;
		ptrs = ptrs->next->next;
		if (!ptr || !ptrs)
			return (0);
		if (ptrs->next == ptr)
			return (1);
	}
	return (0);
}
