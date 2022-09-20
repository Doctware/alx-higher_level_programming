#include "lists.h"

/**
 * check_cycle - checks if a single linked list has a cycle in it.
 * @list: pointer to head of list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *trail, *lead;

	if (list == NULL || list->next == NULL)
		return (0);
	trail = list->next;
	lead = list->next->next;
	while (trail && lead && lead->next)
	{
		if (trail == lead)
			return (1);
		trail = trail->next;
		lead = lead->next->next;
	}

	return (0);
}
