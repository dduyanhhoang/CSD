import pytest
from data_structures.linked_list import LinkedList, Node
from data_structures.exceptions import NodeNotFoundError

def test_init():
	ll = LinkedList()
	assert len(ll) == 0
	assert ll.head is None


def test_insert_first():
	ll = LinkedList()
	ll.insert_first(0)
	assert len(ll) == 1
	assert ll.head.data == 0


def test_search_node_by_value():
    ll = LinkedList()
    ll.insert_first(1)
    ll.insert_first(2)
    ll.insert_first(3)
    assert ll.search_node_by_value(1).data == 1
    assert ll.search_node_by_value(2).data == 2
    assert ll.search_node_by_value(3).data == 3
    with pytest.raises(NodeNotFoundError):
        ll.search_node_by_value(4)


def test_insert_after_node():
    ll = LinkedList()
    ll.insert_first(1)
    node_1 = ll.search_node_by_value(1)
    ll.insert_after_node(node_1, 2)
    assert len(ll) == 2
    assert node_1.next.data == 2
    assert ll.head.data == 1
    assert ll.head.next.data == 2


def test_insert_last():
	ll = LinkedList()
	ll.insert_last(0)
	assert len(ll) == 1
	assert ll.head.data == 0
	ll.insert_first(1)
	ll.insert_first(2)
	ll.insert_first(3)
	ll.insert_last(4)
	assert len(ll) == 5
	assert ll.search_node_by_value(0).next.data == 4
	assert ll.search_node_by_value(4).next is None
