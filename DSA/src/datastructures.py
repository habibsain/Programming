#This module includes all custom datastructure classes essential in algorithms

#Basic python datastructures
#List
#Dict
#Set
#Class

#What we need to build
#Queue
#Stack
#BST
#Min-Heap & Max-Heap tree
#AVL tree
#B-tree
#Hash table
#Disjoint Set Union
##with-> separate chaining, linear probing, quadratic probing, double hashing

class MaxHeap:
    def __init__(self):
        self.heap = []

    def swap_up(self, index):
        #If parent is smaller than child swap
        #arr = self.heap
        parent = (index - 1) // 2
        if parent < 0:
            return
        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            #print(self.heap)
            self.swap_up(parent)

    def swap_down(self, index):
        #If parent is smaller than child swap
        arr = self.heap
        l = len(arr)
        max = index
        child1 = 2 * index + 1
        child2 = 2 * index + 2
        if child1 < l and arr[child1] > arr[max]:
            max = child1

        if child2 < l and arr[child2] > arr[max]:
            max = child2

        if max != index:
            arr[max], arr[index] = arr[index], arr[max]
            self.swap_down(max)

    def insert_node(self, val):
        #Insert at end and until it reaches proper position swap_up
        self.heap.append(val)
        i = len(self.heap) - 1
        self.swap_up(i)

    def extract_max(self):
        #return the root node 
        #replace the root node with last node and swap down
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.swap_down(0)

        return root
    
class MinHeap:
    def __init__(self):
        self.heap = []

    def swap_up(self, index):
        #If parent is greater than child swap
        #arr = self.heap
        parent = (index - 1) // 2
        if parent < 0:
            return
        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            #print(self.heap)
            self.swap_up(parent)

    def swap_down(self, index):
        #If parent is smaller than child swap
        arr = self.heap
        l = len(arr)
        min = index
        child1 = 2 * index + 1
        child2 = 2 * index + 2
        if child1 < l and arr[child1] < arr[min]:
            min = child1

        if child2 < l and arr[child2] < arr[min]:
            min = child2

        if min != index:
            arr[min], arr[index] = arr[index], arr[min]
            self.swap_down(min)

    def insert_node(self, val):
        #Insert at end and until it reaches proper position swap_up
        self.heap.append(val)
        i = len(self.heap) - 1
        self.swap_up(i)

    def extract_min(self):
        #return the root node 
        #replace the root node with last node and swap down
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.swap_down(0)

        return root


# class dsu:
#     def __init__(self):
        


if __name__ == "__main__":
    numList1 = [2, 4, 8, 1, 9, 10, 1.3, 3]
    max_hp = MaxHeap()
    for item in numList1:
        max_hp.insert_node(item)
        print(max_hp.heap)
