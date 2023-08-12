#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted
 * singly linked list
 * @head: pointer to the first node
 * @number: an integer
 * Return: the entire list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	if ((*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	ptr = *head;
	while (ptr->next)
	{
		if (ptr->next->n >= number)
		{
			node->next = ptr->next;
			break;
		}
		ptr = ptr->next;
	}
	ptr->next = node;
	return (*head);
}
