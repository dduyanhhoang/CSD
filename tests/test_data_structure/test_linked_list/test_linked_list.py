import pytest
from data_structures.linked_list import LinkedList, Node

def test_init():
	ll = LinkedList()
	assert len(ll) == 0
	assert ll.head is None


def test_insert_first():
	ll = LinkedList()
	ll.insert_first(0)
	assert len(ll) == 1
	assert ll._head.data == 0
