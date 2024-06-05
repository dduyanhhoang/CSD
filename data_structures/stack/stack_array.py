from data_structures.array import DynamicArray


class StackArray(DynamicArray):
	def __init__(self):
		super().__init__()

	def __len__(self) -> int:
		return self.index

	def push(self, value) -> None:
		self.insert(0, value)

	def pop(self) -> any:
		if self.index == 0:
			raise ValueError('stack is empty')

		data = self[0]
		self.remove_by_index(0)
		return data

	def top(self) -> any:
		if self.index == 0:
			raise ValueError('stack is empty')

		return self[0]

	def have_size(self) -> int:
		return self.index

	def display(self) -> None:
		print(self)
