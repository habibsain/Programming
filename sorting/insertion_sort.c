#include <stdio.h>

/*
    We traverse the array making sure 
    for each position the sub array 
    before it is sorted
*/

void sort(int* arr, int num)
{
    for (int i = 1; i < 5; i++)
    {
        int key = arr[i];
        int j = i - 1;

        //insert arr[i] to sorted array before it
        for (; j >= 0 && arr[j] > key; j--)
        {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;
    }
}

