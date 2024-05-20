import pytest
from data_structures import Array
from data_structures.exceptions import CapacityReachedError


def test_initialization():
    arr = Array(10)
    assert len(arr) == 10
    assert arr.capacity == 10
