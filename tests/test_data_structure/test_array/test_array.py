import pytest
from data_structures import Array
from data_structures.exceptions import CapacityReachedError


def test_initialization():
    arr = Array(10)
    assert len(arr) == 10
    assert arr.capacity == 10

def test_array_insert():
    array = Array(3)
    array.insert(1)
    array.insert(2)
    array.insert(3)

    assert array[0] == 1
    assert array[1] == 2
    assert array[2] == 3

    with pytest.raises(CapacityReachedError):
        array.insert(4)
