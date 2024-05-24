from typing import Optional
from .node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value):
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
    
    def __len__(self):
        return self.size

    def insert_first(self, value) -> None:
        new_first = Node(value, self._head)
        self._head = new_first
        self._size += 1
