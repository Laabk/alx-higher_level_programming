#include "lists.h"

/**
 * insert_node - this func inserts a new node to de struc
 * at a given position.
 * @head: the head of the linked list
 * @number: the index of loc of added node
 * Return: new node location, or NULL for not availble
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *dnew_nod, *h, *befr;

	h = *head;
	dnew_nod = malloc(sizeof(listint_t));

	if (dnew_nod == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		befr = h;
		h = h->next;
	}

	dnew_nod->n = number;

	if (*head == NULL)
	{
		dnew_nod->next = NULL;
		*head = dnew_nod;
	}
	else
	{
		dnew_nod->next = h;
		if (h == *head)
			*head = dnew_nod;
		else
			befr->next = dnew_nod;
	}

	return (dnew_nod);
}
