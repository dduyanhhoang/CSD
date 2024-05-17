# Array structure:
# +data[]
# +index
# +capacity
#
# -insert(value)
# -delete(index)
# -update(index, value)
#     check -> delete -> insert?
# -search(value) -> bool
# -display()

class IntArray:
    def __init__(self, index: int, capacity: int, data: list):
        self.index = index
        self.capacity = capacity
        self.data = data

    def insert(self, value: int) -> bool:
        if self.index + 1 == self.capacity:
            return False
        self.data[self.index + 1] = value
        self.index += 1
        return True

    def delete_by_index(self, index) -> bool:
        if not (0 <= index <= self.index):
            return False

        update_index = 0
        for i in range(index, self.index - 1):
            self.data[i] = self.data[i + 1]
            update_index += 1

        self.data[self.index] = None
        self.index -= update_index
        return True

    def delete_by_value(self, value) -> bool:
        for i in range(self.index):
            if value == self.data[i]:
                self.delete_by_index(i)
                return True

        return False

    def update(self, index: int, new_value: int) -> bool:
        if not (0 <= index <= self.index):
            return False

        for i in range(self.index):
            if i == index:
                self.data[i] = new_value
                return True

        return False

    def display(self) -> None:
        for i in self.data[:self.index]:
            print(i, end=' ')

        print()

    def search(self, value: int) -> bool:
        for i in range(self.index):
            if self.data[i] == value:
                return True

        return False


int_array = IntArray(4, 20, [1, 2, 3, 4])
int_array.display()
