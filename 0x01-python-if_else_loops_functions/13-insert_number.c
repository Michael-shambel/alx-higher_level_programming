#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *repr = *head;
	listint_t *node = NULL;
	
	if (!head)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	
	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n){
		node->next = *head;
		*head = node;
		return node;
	}
	while (repr->next != NULL && repr->next->n < number)
	{
		repr = repr->next;
	}

	node->next = repr->next;
	repr->next = node;

	return node;
}
