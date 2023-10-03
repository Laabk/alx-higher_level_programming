#include "lists.h"

/**
 * check_cycle - checks to ensure linked list has a cycle
 * @list: the linked list that is going to be check
 * Return: if 1 list has cycle, if 0 it no any cycle
 *
 */

int check_cycle(listint_t *list)
{
		listint_t *rates = list, *spd = list;

		if (!list)
		return (0);

		while (rates && sped && sped->next)
		{
		rates = rates->next;
		sped = sped->next->next;
		if (rates == sped)
		return (1);
		}
		return (0);
}
