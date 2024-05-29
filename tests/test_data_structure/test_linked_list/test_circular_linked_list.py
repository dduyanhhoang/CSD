import pytest
from data_structures.linked_list import CircularLinkedList, Node
from data_structures.exceptions import NodeNotFoundError


def test_init():
	cll = CircularLinkedList()
	assert len(cll) == 0
	assert cll.last is None


def test_insert_first():
	cll = CircularLinkedList()
	cll.insert_first(1)
	assert len(cll) == 1
	assert cll.last.next.data == 1
	cll.insert_first(2)
	assert cll.last.next.data == 2


def test_insert_last():
	cll = CircularLinkedList()
	cll.insert_last(1)
	assert len(cll) == 1
	assert cll.last.data == 1
	assert cll.last.next.data == 1
	cll.insert_last(2)
	assert len(cll) == 2
	assert cll.last.data == 2
	assert cll.last.next.data == 1


def test_search_node_by_value():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(2)
	cll.insert_last(3)
	cll.insert_last(4)
	assert cll.search_node_by_value(2).data == 2
	assert cll.search_node_by_value(2).next.data == 3


def test_insert_after_node():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(2)
	cll.insert_last(4)
	cll.insert_after_node(cll.search_node_by_value(2), 3)
	assert len(cll) == 4
	assert cll.search_node_by_value(2).next.data == 3
	assert cll.search_node_by_value(3).data == 3
	assert cll.search_node_by_value(3).next.data == 4
	assert cll.last.data == 4
	assert cll.last.next.data == 1


def test_update_node():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(3)
	cll.insert_last(4)

	cll.update_node(cll.search_node_by_value(3), 2)
	assert len(cll) == 3
	assert cll.search_node_by_value(1).next.data == 2
	assert cll.search_node_by_value(2).next.data == 4

	cll.update_node(cll.search_node_by_value(4), 3)
	assert len(cll) == 3
	assert cll.search_node_by_value(2).next.data == 3
	assert cll.last.data == 3


def test_delete_first():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(2)
	cll.insert_last(3)

	cll.delete_first()
	assert len(cll) == 2
	assert cll.last.next.data == 2

	cll.delete_first()
	cll.delete_first()
	with pytest.raises(ValueError):
		cll.delete_first()


def test_delete_after_node():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(2)
	cll.insert_last(4)
	cll.insert_last(3)

	cll.delete_after_node(cll.search_node_by_value(2))
	assert len(cll) == 3
	assert cll.search_node_by_value(2).next.data == 3

	cll.delete_after_node(cll.search_node_by_value(1))
	cll.delete_after_node(cll.search_node_by_value(1))
	cll.delete_after_node(cll.search_node_by_value(1))
	assert len(cll) == 0
	assert cll.last is None

def test_delete_last():
	cll = CircularLinkedList()
	cll.insert_last(1)
	cll.insert_last(2)
	cll.insert_last(3)

	cll.delete_last()
	assert len(cll) == 2
	assert cll.last.data == 2
	assert cll.last.next.data == 1

	cll.delete_last()
	cll.delete_last()
	with pytest.raises(ValueError):
		cll.delete_last()	
