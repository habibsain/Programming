#import pytest as pt
from src import algorithms
def hello(x: str):
    y = x.lower()
    if y == "hello":
        return True
    return False

def test_hello():
    assert hello("HELLo") == True

num_list = [2, 4, 8, 1, 9, 10, 1.3, 3]

def test_partition():
    pass

def test_quicksort():
    pass
    


# if __name__ == "main":
#     pass