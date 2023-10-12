#include "lists.h"

/**
 * dlistint_len - the number of elements present in
 * a double linked list
 * @h: the head of list
 * Return: number of nodes present
 */

size_t dlistint_len(const dlistint_t *h)
{
	int numb = 0;

	if (h == NULL)
	return (numb);

	while (h->prev != NULL)
	h = h->prev;
	while (h != NULL)
	{
	numb++;
	h = h->next;
	}
	return (numb);
}
