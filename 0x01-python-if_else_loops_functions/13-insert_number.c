#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert number into a sorted singly linked list
 * @head: pinting to the head of the node
 * @nuber: number to be inserted
 * Return: surted number
 */

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *current = *head;

	listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}

	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}

