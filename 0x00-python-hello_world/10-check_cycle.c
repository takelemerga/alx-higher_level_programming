#include "lists.h"

/**
 *check_cycle - checks if there a cycle in a linked list
 *It uses the floyed-cycle algorithm
 *@list: head of the linked least
 *Return: 1 if there is a loop, 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *nextnode = NULL;

	if (!list)
		return (0);
	nextnode = list->next;

	while (nextnode && nextnode->next)
	{
		/*if there is a loop they would crush*/
		if (nextnode == list)
			return (1);
		nextnode = nextnode->next->next;
		list = list->next;
	}
	return (0);
}
