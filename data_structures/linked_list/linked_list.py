from .node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def insert_first(self, value):
        self._head = Node(value, self._head)
        self._size += 1

    def insert_last(self, value):
        if self._size == 0:
            self.insert_first(value)
        else:
            last_node = self._head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(value)
            self._size += 1

    def insert_after_node(self, target_node, value):
        if self._size == 0:
            raise Exception('linked list is empty')
        else:
            current_node = self._head
            while current_node and current_node != target_node:
                current_node = current_node.next
            if current_node is None:
                raise Exception('Node not found in the list')
            new_node = Node(value, current_node.next)
            current_node.next = new_node
            self._size += 1

    def delete_first(self):
        if self._size == 0:
            raise Exception('linked list is empty')

        old_head_node = self._head
        self._head = self._head.next

        old_head_node.next = None
        self._size -= 1

    def delete_after_node(self, target_node):
        if self._size == 0:
            raise Exception('linked list is empty')
        current_node = self._head
        while current_node and current_node != target_node:
            current_node = current_node.next
        if current_node is None or current_node.next is None:
            raise Exception('Node not found or has no next node')
        current_node.next = current_node.next.next
        self._size -= 1

    def delete_last(self):
        if self._size == 0:
            raise Exception('linked list is empty')
        if self._size == 1:
            self._head = None
        else:
            current_node = self._head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None
        self._size -= 1

    def update(self, target_node, value):
        current_node = self._head
        while current_node and current_node != target_node:
            current_node = current_node.next
        if current_node is None:
            raise Exception('Node not found in the list')
        current_node.value = value

    def search(self, value):
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def __str__(self):
        nodes = []
        current_node = self._head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        return " -> ".join(nodes)
