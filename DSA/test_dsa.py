#import pytest as pt
from src import algorithms, datastructures
def hello(x: str):
    y = x.lower()
    if y == "hello":
        return True
    return False

def test_hello():
    assert hello("HELLo") == True

numList1 = [2, 4, 8, 1, 9, 10, 1.3, 3]
numList2 = [2, 4, 8, 1, 9, 10, 1.3, 5]

l1 = 0
r1 = len(numList1) - 1

l2 = 0
r2 = len(numList2) - 1

#[2, 1, 1.3, 3, 4, 8, 9, 10]

def test_partition():
    assert algorithms.partition(numList1, l1, r1) == 3
    assert algorithms.partition(numList2, l2, r2) == 4

def test_quicksort():
    algorithms.quicksort(numList1, 0, len(numList1) - 1)
    assert  numList1 == [1, 1.3, 2, 3, 4, 8, 9, 10]
    algorithms.quicksort(numList2, 0, len(numList2) - 1)
    assert  numList2 == [1, 1.3, 2, 4, 5, 8, 9, 10]

def test_maxHeap():
    hp = datastructures.MaxHeap()
    for item in numList1:
        hp.insert_node(item)

    assert hp.extract_max() == 10
    assert hp.extract_max() == 9
    assert hp.extract_max() == 8
    assert hp.extract_max() == 4

def test_minHeap():
    hp1 = datastructures.MinHeap()
    for item in numList1:
        hp1.insert_node(item)

    assert hp1.extract_min() == 1
    assert hp1.extract_min() == 1.3
    assert hp1.extract_min() == 2
    assert hp1.extract_min() == 3


# if __name__ == "main":
#     pass