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
##with-> separate chaining, linear probing, quadratic probing, double hashing

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert_node(self):
        #Insert at end and until it reaches proper position swap_up
        pass

    def swap_up(self, arr: list[int | float], index):
        #If parent is smaller than child swap
        parent = (index - 1) // 2
        if arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            self.swap_up(arr, index)

    def swap_down(self, arr: list[int | float], index):
        #If parent is smaller than child swap
        max = index
        if arr[2 * index + 1] > arr[max]:
            max = 2 * index + 1

        if arr[2 * index + 2] > arr[max]:
            max = 2 * index + 2


        if max != index
            arr[max], arr[index] = arr[index], arr[max]
            self.swap_down(arr, index)

    def extract_max(self):
        #return the root node 
        #replace the root node with last node and swap down




if __name__ == "__main__":
    pass