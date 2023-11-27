#include "lists.h"

/**
 *check_cycle - check if singly linked list has cycle
 *@list: pointer list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *makeshift = list;

	while (makeshift != NULL && makeshift->next != NULL)
	{
		list = list->next;

		makeshift = makeshift->next->next;

		if (list == makeshift)
			return (1);
	}
	return (0);
}
