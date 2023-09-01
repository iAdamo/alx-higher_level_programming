#!/usr/bin/python3
"""defining a node of a singly linked list"""


class Node:
    """class Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initialization of instance attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter property to data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """setter property to data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter property to next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter property to next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initialize head to None"""
        self.__head = None

    def __str__(self):
        """initialise a current attribute for traversing the head"""
        current = self.__head
        node_data = []
        while current:
            node_data.append(str(current.data))
            current = current.next_node
        return "\n".join(node_data)

    def sorted_insert(self, value):
        """sorted_insert -  inserts a new Node into the
        correct sorted position in the list (increasing order)"""
        new_node = Node(value)

        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
