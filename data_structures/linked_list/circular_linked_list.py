from typing import Optional
from .node import Node
from data_structures.exceptions import NodeNotFoundError

class CircularLinkedList:
	def __init__(self):
		self._last = None
		self._size = 0

	@property
	def size(self) -> int:
		return self._size

	@size.setter
	def size(self, value: int) -> None:
		if value < 0:
			raise ValueError('linnked list size could not be negative')
		self._size = value

	@property
	def last(self) -> Optional['Node']:
		return self._last

	@last.setter
	def last(self, target_node: Optional['Node']) -> None:
		if not (target_node is None or isinstance(target_node, Node)):
			raise TypeError('last must be a Node or None')
		self._last = target_node

	def __len__(self) -> int:
		return self.size

	def insert_first(self, value: any) -> None:
		if self.size == 0:
			tmp_node = Node(value, None)
			tmp_node.next = tmp_node
			self.last = tmp_node
			self.size += 1
		else:
			tmp_node = Node(value, self.last.next)
			self.last.next = tmp_node
			self.size += 1

	def insert_last(self, value: any) -> None:
		if self.size == 0:
			tmp_node = Node(value, None)
			tmp_node.next = tmp_node
			self.last = tmp_node
			self.size += 1
		else:
			tmp_node = Node(value, self.last.next)
			self.last.next = tmp_node
			self.last = tmp_node
			self.size += 1

	def search_node_by_value(self, value: any) -> Node:
		if self.size == 0:
			raise NodeNotFoundError("Circular linked list is empty")
		track_node = self.last.next
		while True:
			if track_node.data == value:
				return track_node
			track_node = track_node.next
			if track_node == self.last.next:
				raise NodeNotFoundError(f"Node with value '{value}' not found")

	def insert_after_node(self, target_node: Node, value: any) -> None:
		if not target_node:
			raise ValueError('target_node could not be None')

		if not isinstance(target_node, Node):
			raise TypeError('target_node must be a Node')

		new_node = Node(value, target_node.next)
		target_node.next = new_node
		self.size += 1

	def update_node(self, target_node: Node, value: any) -> bool:
		if not target_node:
			raise ValueError('target_node could not be None')

		if not isinstance(target_node, Node):
			raise TypeError('target_node must be a Node')

		track_node = self.last.next
		while True:
			if track_node == target_node:
				target_node.data = value
				return True
			track_node = track_node.next
			if track_node == self.last.next:
				raise NodeNotFoundError()

	def delete_first(self) -> None:
		if self.size == 0:
			raise ValueError('CircularLinkedList is empty')

		if self.size == 1:
			self.last.next == None
			self.last = None
			self.size -= 1
		else:
			old_first = self.last.next
			self.last.next = old_first.next
			old_first.next = None
			self.size -= 1

	def delete_after_node(self, target_node: Node) -> None:
		if not target_node:
			raise ValueError('target_node could not be None')
		if not isinstance(target_node, Node):
			raise TypeError('target_node must be a Node')
		if self.size == 0:
			raise ValueError('CircularLinkedList is empty')

		tmp_node = target_node.next
		if tmp_node == self.last:
			self.last = target_node
		if tmp_node == target_node:
			self.last = None
		target_node.next = tmp_node.next
		tmp_node.next = None
		if tmp_node == self.last:
			self.last = target_node
		self.size -= 1

	def delete_last(self) -> None:
		if self.size == 0:
			raise ValueError('CircularLinkedList is empty')

		if self.size == 1:
			self.last.next == None
			self.last = None
			self.size -= 1
		else:
			old_last = self.last

			penultimate_node = self.last.next
			while penultimate_node.next != self.last:
				penultimate_node = penultimate_node.next

			penultimate_node.next = self.last.next
			old_last.next = None
			self.last = penultimate_node
			self.size -= 1

	def __str__(self) -> str:
		return ''

	def show_linked_list(self) -> None:
		pass
