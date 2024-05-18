import pytest
from data_structures import DynamicArray


def test_initialization():
    darr = DynamicArray()
    assert len(darr) == 0
    assert darr.capacity == 1


def test_append():
    darr = DynamicArray()
    darr.append(1)
    assert len(darr) == 1
    assert darr[0] == 1
    darr.append(2)
    assert len(darr) == 2
    assert darr[1] == 2
    darr.append(3)
    assert len(darr) == 3
    assert darr[2] == 3
    assert darr.capacity == 4


def test_get_item():
    darr = DynamicArray()
    darr.append(1)
    darr.append(2)
    darr.append(3)
    assert darr[0] == 1
    assert darr[1] == 2
    assert darr[2] == 3
    with pytest.raises(IndexError):
        _ = darr[3]
    with pytest.raises(IndexError):
        _ = darr[-1]
    with pytest.raises(IndexError):
        _ = darr[1.1]
    with pytest.raises(IndexError):
        _ = darr["1"]


def test_insert():
    darr = DynamicArray()
    darr.append(1)
    darr.append(3)
    darr.insert(1, 2)
    assert len(darr) == 3
    assert darr[0] == 1
    assert darr[1] == 2
    assert darr[2] == 3
    darr.insert(0, 0)
    assert darr[0] == 0
    assert darr[1] == 1
    with pytest.raises(IndexError):
        darr.insert(1.1, 1)
    with pytest.raises(IndexError):
    	darr.insert('1', 1)


def test_remove_by_value():
    darr = DynamicArray()
    darr.append(1)
    darr.append(2)
    darr.append(3)
    darr.remove_by_value(2)
    assert len(darr) == 2
    assert darr[0] == 1
    assert darr[1] == 3
    with pytest.raises(ValueError):
        darr.remove_by_value(4)


def test_remove_by_index():
    darr = DynamicArray()
    darr.append(1)
    darr.append(2)
    darr.append(3)
    darr.remove_by_index(1)
    assert len(darr) == 2
    assert darr[0] == 1
    assert darr[1] == 3
    with pytest.raises(IndexError):
    	darr.remove_by_index(3)
    with pytest.raises(IndexError):
    	darr.remove_by_index(1.1)


def test_get_item():
    darr = DynamicArray()
    darr.append(1)
    darr.append(2)
    darr.append(3)
    assert darr[0] == 1
    assert darr[1] == 2
    assert darr[2] == 3
    with pytest.raises(IndexError):
        _ = darr[3]
    with pytest.raises(IndexError):
    	_ = darr[1.1]
    with pytest.raises(IndexError):
    	_ = darr['1']


def test_str_representation():
    darr = DynamicArray()
    darr.append(1)
    darr.append(2)
    darr.append(3)
    assert str(darr) == "[ 1, 2, 3 ]"
