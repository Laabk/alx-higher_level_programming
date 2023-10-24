#!/usr/bin/python3
"""a singly linked list"""


class Node:
    """defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """the data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """initialise the data attribute"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """returns the next_node attribute
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """takes next node val"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines the singly linked list"""

    def __init__(self):
        """Initializes singly linked list"""

        self.head = None

    def __str__(self):

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted list"""

        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
