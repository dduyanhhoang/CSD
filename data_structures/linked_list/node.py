from typing import Optional

class Node:
    def __init__(self, data: any, next: Optional['Node'] = None):
        self.data = data
        self.next = next

    @property
    def data(self) -> any:
        return self._data
    
    @data.setter
    def data(self, data: any) -> None:
        self._data = data

    @property
    def next(self) -> Optional['Node']:
        return self._next
    
    @next.setter
    def next(self, target_node: Optional['Node']) -> None:
        if not (target_node is None or isinstance(target_node, Node)):
            raise TypeError("next must be a Node or None")

        self._next = target_node
