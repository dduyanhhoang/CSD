import ctypes                                           # provide low-level arrays

class DynamicArray:
    def __init__(self):
        self._index = 0
        self._capacity = 1
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
        self._capacity = value

    def __len__(self):
        return self.index

    def __getitem__(self, index):
        if not (isinstance(index, int) and 0 <= index < self.index):
            raise IndexError('invalid index')
        return self._array[index]

    def append(self, obj):
        if self.index == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self.index] = obj
        self.index += 1

    def _resize(self, new_capacity):
        temp_arr = self._make_array(new_capacity)
        for k in range(self.index):
            temp_arr[k] = self._array[k]
        self._array = temp_arr
        self.capacity = new_capacity

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, index: int, value) -> None:
        if not (isinstance(index, int) and 0 <= index <= self.index):
            raise IndexError('invalid index')

        if self.index == self.capacity:
            self._resize(2 * self.capacity)

        for j in range(self.index, index, -1):
            self._array[j] = self._array[j - 1]

        self._array[index] = value
        self.index += 1

    def remove_by_value(self, value) -> None:
        for k in range(self.index):
            if self._array[k] == value:
                self.remove_by_index(k)
                return
        raise ValueError('value not found')

    def remove_by_index(self, index: int) -> None:
        if not (0 <= index < self.index and isinstance(index, int)):
            raise IndexError('invalid index')

        for j in range(index, self.index - 1):
            self._array[j] = self._array[j + 1]
        self._array[self.index - 1] = None
        self.index -= 1

    def __str__(self) -> str:
        darr_str = "["

        for i in range(self.index):
            darr_str += f" {self._array[i]},"
        darr_str = darr_str.rstrip(',')
        darr_str += " ]"

        return darr_str
