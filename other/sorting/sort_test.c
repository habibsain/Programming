#include <stdio.h>
//#include "insertion_sort.h"
#include "merge_sort.h"

void print_arr(int* arr, int num)
{
    for (int i = 0; i < num; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void merge_test()
{
    int arr1[] = {1, 3, 4, 7, 2, 5, 6};
    merge(arr1, 0, 3, 6);
    assert();
}

int main()
{
    int num = 5;
    int arr[] = {2, 4, 1, 5, 3};

    //print array
    print_arr(arr, num);
    sort(arr, num);

    //print sorted array
    print_arr(arr, num);

    return 0;
}