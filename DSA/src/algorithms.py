#Algorithms to be included are->
#Sorting->bubble,selection,Insertion,merge,quick,heap
#Graph->
#Shortest path problem->bfs, dijkstra's, bellmanford, 


#-------helper functions---------#

#places the last element to it's correct position    
def partition(num_list: list[int | float], low: int, high: int):
    r = high
    i = low - 1
    j = low
    x = num_list[high]
    while(j < r):
        if(num_list[j] < x):
            i = i + 1
            num_list[i], num_list[j] = num_list[j], num_list[i]
        j = j + 1
    num_list[i + 1], num_list[r] = num_list[r], num_list[i+1]
    return i + 1

# class Sort():
#     def __init__(self, num_list: list[int | float]):
#         self.num_list = num_list
#         self.start = 0
#         self.length = len(num_list)
#         self.end = len(num_list) - 1

#     def quicksort(p, r):
#         pass
        


def quicksort(num_list: list[int | float], low: int , high: int)-> None:
    # p = 0
    # r = len(num_list) - 1
    if(low < high):
        q = partition(num_list, low, high)
        quicksort(num_list, low, q - 1)
        quicksort(num_list, q + 1, high)
    # return [2, 4, 8, 1, 9, 10, 1.3, 3]




if __name__ == "__main__":
    numList = [2, 4, 8, 1, 9, 10, 1.3, 3]
    x = partition(numList, 0, len(numList) - 1)
    print(x)