#include <stdio.h>

void sort(int* arr, int num)
{
    for (int i = 1; i < 5; i++)
    {
        int key = arr[i];
        int j = i - 1;

        //insert arr[i] to sorted array before it
        for (j = i - 1; j >= 0 && arr[j] > key; j--)
        {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;
    }
}

void print_arr(int* arr, int num)
{
    for (int i = 0; i < num; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
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