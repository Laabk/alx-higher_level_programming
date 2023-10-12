#include "lists.h"

/**
 * print_dlistint - this prints elements present in
 * the dlistint_t list
 * @h: the head of the dlistint_t list
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int numb = 0;

	if (h == NULL)
	return (numb);

	while (h->prev != NULL)
	h = h->prev;
	while (h != NULL)
	{
	printf("%d\n", h->n);
	numb++;
	h = h->next;
	}
	return (numb);
}

