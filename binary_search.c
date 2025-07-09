//binary_search.c


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int search(int* nums,  int numSize, int target){
	//Write your code here....
	//If found return the index
	//Else return -1
	
	return 2;//Trial
}

void* merge(int* arr, int left, int mid, int right)
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

void mergesort(int* arr, int left,  int right)
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
	int elem_num =  sizeof(nums);
	printf("Number of elements is %d\n", elem_num);
}

int main(int argc, char** argv)
{
	int numSize, *nums;


	if (argc >= 2)
	{
		numSize = argc - 1;
		nums = malloc(sizeof(int) * numSize);
		for(int i = 0; i < numSize; i++)
		{
			nums[i] = atoi(argv[i+1]);
		}
	}
	else
	{
		printf("Enter the numberr of elements in search array:");
		scanf("%d", &numSize);
		nums = malloc(sizeof(int) * numSize);
		
		printf("Enter the array  elements separated by spaces:\n");
		
		for(int i = 0; i < numSize; i++)
		{
			scanf("%d", nums + i);
		}
	}

	int target;
	printf("Enter the target element you want to search:\n");
	scanf("%d", &target);

	//Binary Search
	int index;
	sort(nums, numSize);
	index = search(nums, numSize, target);
		
	printf("The index of %d is %d\n", target, index);
	for(int i = 0; i < numSize; i++)
                {
                        printf("%d \t", nums[i]);
                }
	printf("\n");
	free(nums);
        nums = NULL;


	return 0;
}
