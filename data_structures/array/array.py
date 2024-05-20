from data_structures.exceptions import CapacityReachedError
import ctypes


class Array:
	def __init__(self, capacity: int):
		self.index = 0
		self.capacity = capacity
		self._array = self._make_array(self.capacity)

	@property
	def index(self):
		return self._index

	@index.setter
	def index(self, value: int):
		self._index = value

	@property
	def capacity(self):
		return self._capacity
	
	@capacity.setter
	def capacity(self, value: int):
		if not (isinstance(value, int) and 0 < value):
			raise ValueError("Invalid capacity")
		self._capacity = value

	def __len__(self) -> int:
		return self.capacity

	def __getitem__(self, index):
		if not (isinstance(index, int) and 0 <= index < self.index):
			raise IndexError('invalid index')
		return self._array[index]

	def _make_array(self, capacity: int):
		return (capacity * ctypes.py_object)()

	def insert(self, index: int, value):
		if self.index == self.capacity:
			raise CapacityReachedError()

		if not (isinstance(index, int) and 0 <= index <= self.index):
			raise IndexError('invalid index')

		self._array[self.index] = obj
		self.index += 1

	def remove_by_value(self, value) -> None:
		for k in range(self.index):
			if self._array[i] == value:
				self.remove_by_index()
				return
		raise ValueError('value not found')

	def remove_by_index(self, index: int) -> None:
		if not (isinstance(index, int) and 0 <= index <= self.index):
			raise IndexError('invalid index')

		for i in range(index, self.index - 1):
			self._array[i] = self._array[i + 1]

		self._array[self.index - 1] = None
		self._index -= 1

	def __str__(self) -> str:
		darr_str = "["
		for i in range(self.index):
			darr_str += f" {self._array[i]},"
		darr_str = darr_str.rstrip(',')
		darr_str += " ]"
		return darr_str
		