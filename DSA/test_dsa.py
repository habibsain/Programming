#import pytest as pt
from src import algorithms
def hello(x: str):
    y = x.lower()
    if y == "hello":
        return True
    return False

def test_hello():
    assert hello("HELLo") == True

numList1 = [2, 4, 8, 1, 9, 10, 1.3, 3]
numList2 = [2, 4, 8, 1, 9, 10, 1.3, 5]

#[2, 1, 1.3, 3, 4, 8, 9, 10]

def test_partition():
    assert algorithms.partition(num_list=numList1) == 3
    assert algorithms.partition(num_list=numList2) == 4

def test_quicksort():
    assert algorithms.quicksort(numList1) == [1, 1.3, 2, 3, 4, 8, 9, 10]
    


# if __name__ == "main":
#     pass