#Algorithms to be included are->
#Sorting->bubble,selection,Insertion,merge,quick,heap
#Graph->
#Shortest path problem->bfs, dijkstra's, bellmanford, 


#-------helper functions---------#

def swap(x: any, y: any)->None:
    temp: any = x
    x = y
    y = temp

#places the last element to it's correct position    
def partition(num_list: list[int | float])-> list[int | float]:
    p = 0
    r = len(num_list) - 1
    i = p - 1
    j = p
    x = num_list[r]
    while(j < r):
        if(num_list[j] < x):
            i = i + 1
            swap(num_list[i], num_list[j])
        j = j + 1
    swap(num_list[i + 1], num_list[r])
    return i + 1

class Sort():
    def __init__(self, num_list: list[int | float]):
        self.num_list = num_list
        self.start = 0
        self.length = len(num_list)
        self.end = len(num_list) - 1

    def quicksort(p, r):
        


def quicksort(num_list: list[int | float], r: int, p: int = 0,)-> list[int | float]:
    p = 0
    r = len(num_list) - 1
    if(p < r):
        q = partition(num_list)
    return [2, 4, 8, 1, 9, 10, 1.3, 3]




if __name__ == "main":
    numList = [2, 4, 8, 1, 9, 10, 1.3, 3]
    x = partition(numList)
    print(x)