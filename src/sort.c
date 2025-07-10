//sort.c

#include "../include/sort.h"

static void merge(int* arr, int left, int mid, int right)
{
	int i = left;
	int j = mid + 1;
	int temp[right +1];
	int k = 0;
	while (i <= mid && j <= right)
	{
		if (arr[i] < arr[j])
			temp[k++] = arr[i++];
		
		else
			temp[k++] = arr[j++];
		
	}

	while (i <= mid)
	{
		temp[k++] = arr[i++];
	}

	while (j <= right)
	{
		temp[k++] = arr[j++];
	}
	
}

static void mergesort(int* arr, int left,  int right)
{
	int mid = left + (right - left)/2;
	int left_arr[mid];
	int right_arr[right - mid];

	mergesort(arr, left, mid );
	mergesort(arr, mid + 1, right);
	merge(arr, left, mid, right);
}

void sort(int* nums, int numSize)
{
	//Write a merge sort algorithm
	int left = 0;
	int right = numSize - 1;
	mergesort(nums, left, right);
}