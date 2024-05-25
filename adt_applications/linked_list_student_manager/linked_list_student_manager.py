from .student import Student
from data_structures.linked_list import LinkedList 
from data_structures.linked_list import Node
from data_structures.exceptions import NodeNotFoundError
from typing import Optional

class LinkedListStudentManager(LinkedList):
	def __init__(self):
		super().__init__()

	def student_exist(self, id: str) -> bool:
	    track_node = self.head
	    while track_node:
	        if track_node.data.id == id:
	            return True
	        track_node = track_node.next
	    return False

	def insert_first(self, student: Student) -> None:
		if not isinstance(student, Student):
			raise ValueError('inserting data must be a Student')

		if self.student_exist(student.id):
			raise ValueError(f"student with id '{student.id}' already exist")

		super().insert_first(student)

	def insert_last(self, student: Student) -> None:
		if not isinstance(student, Student):
			raise ValueError('inserting student must be a Student')

		if self.student_exist(student.id):
			raise ValueError(f"student with id '{student.id}' already exist")

		super().insert_last(student)

	def search_student_by_name(self, name: str) -> Node:
		track_node = self.head
		while track_node:
			if track_node.data.name == name:
				return track_node
			track_node = track_node.next
		raise NodeNotFoundError(f"student with name '{name}'' not found")

	def search_student_by_id(self, id: str) -> Node:
		track_node = self.head
		while track_node:
			if track_node.data.id == id:
				return track_node
			track_node = track_node.next
		raise NodeNotFoundError(f"student with id '{id}' not found")

	def update_student_by_id(self, id: str, name: str, mark: float) -> bool:
	    track_node = self.search_student_by_id(id)
	    track_node.data.name = name
	    track_node.data.mark = mark
	    return True

	def delete_first(self) -> None:
		super().delete_first()

	def delete_last(self) -> None:
		super().delete_last()

	def delete_by_id(self, id: str) -> None:
		track_del_node = self.search_student_by_id(id)

		track_node = self.head
		while track_node:
			if track_node.next == track_del_node:
				track_node.next = track_del_node.next
				track_del_node.next = None
				self.size -= 1
				return

	def __str__(self) -> str:
		if self.size == 0:
			return f"*head{'\n|' * 3}\nNone"

		ll_str = "* [head]"
		track_node = self.head
		counter = 0

		while track_node:
			ll_str += f"{'\n|' * 3}\n* [{track_node.data.id}|{track_node.data.name}|{track_node.data.mark}]"
			track_node = track_node.next
			counter += 1

		return ll_str + f"{'\n|' * 3}\n* [None]"

	def display_students(self) -> None:
		print(f"Student manager currently has {self.size} students:")
		print(self)
