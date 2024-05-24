from typing import Optional
from .node import Node

from data_structures.exceptions import NodeNotFoundError


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        if value < 0:
            raise ValueError('linked list size could not be negative')
        self._size = value

    @property
    def head(self) -> Optional['Node']:
        return self._head

    @head.setter
    def head(self, target_node: Optional['Node']) -> None:
        if not (target_node is None or isinstance(target_node, Node)):
            raise TypeError('head must be a Node or None')
        self._head = target_node
    
    def __len__(self) -> int:
        return self.size

    def insert_first(self, value: any) -> None:
        new_first = Node(value, self._head)
        self._head = new_first
        self.size += 1

    def search_node_by_value(self, value: any) -> Node:
        track_node = self._head
        while track_node:
            if track_node.data == value:
                return track_node
            track_node = track_node.next
        raise NodeNotFoundError(value)

    def insert_after_node(self, target_node: Node, value: any) -> None:
        if not target_node:
            raise ValueError('target_node could not be None')

        if not isinstance(target_node, Node):
            raise TypeError('target_node must be a Node')

        new_node = Node(value, target_node.next)
        target_node.next = new_node
        self.size += 1

    def insert_last(self, value: any) -> None:
        if self.head is None:
            self.insert_first(value)
        else:
            last_node = self._head
            while last_node.next is not None:
                last_node = last_node.next
            self.insert_after_node(last_node, value)

    def delete_first(self) -> None:
        if self.size == 0:
            raise ValueError('linked list is empty')

        first_node = self.head
        self._head = self._head.next
        first_node.next = None
        self.size -= 1

    def delete_after_node(self, target_node: Node) -> None:
        if not target_node:
            raise ValueError('target_node could not be None')

        if not isinstance(target_node, Node):
            raise TypeError('target_node must be a Node')

        if target_node.next is None:
            raise ValueError('target_node could not be the last Node')

        node_to_del = target_node.next
        target_node.next = node_to_del.next
        node_to_del.next = None
        self.size -= 1

    def delete_last(self) -> None:
        if self.size == 0:
            raise ValueError('linked list is empty')
        elif self.size == 1:
            self.delete_first()
        else:
            penultimate_node = self.head
            while penultimate_node.next and penultimate_node.next.next:
                penultimate_node = penultimate_node.next
                last_node = penultimate_node.next

            penultimate_node.next = last_node.next
            last_node.next = None
            self.size -= 1
