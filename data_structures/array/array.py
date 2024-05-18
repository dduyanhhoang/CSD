from data_structures.exceptions import CapacityReachedError
import ctypes


class Array:
	def __init__(self, capacity: int):
		self.index = 0
		self.capacity = capacity
		self._array = self._make_array(self.capacity)

	@property
	def capacity(self):
		return self._capacity
	
	@capacity.setter
	def capacity(self, value: int):
		if not (0 < value):
			raise ValueError("Invalid capacity")
		self._capacity = value

	@property
	def index(self):
		return self._index

	@index.setter
	def index(self, value: int):
		self._index = value

	@property
	def array(self):
		return self._array

	def _make_array(self, capacity: int):
		return (capacity * ctypes.py_object)()

	def __len__(self) -> int:
		return self.capacity

	def __getitem__(self, index):
		if not (0 <= index <= self.capacity):
			raise IndexError('invalid index')
		return self._array[index]

	def insert(self, obj):
		if self.index == self.capacity:
			raise CapacityReachedError()
		self._array[self.index] = obj
		self.index += 1
