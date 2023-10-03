#include "lists.h"

/**
 * check_cycle - checks to ensure linked list has a cycle
 * @list: the linked list that is going to be check
 * Return: if 1 list has cycle, if 0 it no any cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *bck = list, *bcks = lsit;

	while (list && bck && bck->next)
	{
		list = list->next;
		bck = bck->next->next;

		if (list == bck)
		{
			list = bcks;
			bcks =  bck;
			while (1)
			{
				bck = bcks;
				while (bck->next != list && bck->next != bcks)
				{
					bck = bck->next;
				}
				if (bck->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
