#!/usr/bin/python3

class Node:
    """Node class defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data: The data to be stored in the node.
        - next_node: The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Raises:
        - TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Raises:
        - TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class defines a singly linked list."""

    def __init__(self):
        """Simple instantiation of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order).

        Parameters:
        - value: The value to be inserted into the list as a new node.
        """
        new_node = Node(value)

        # If the list is empty or the new node should be the new head
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def display(self):
        """Prints the entire list in stdout, one node number per line."""
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node
