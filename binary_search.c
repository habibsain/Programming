//binary_search.c


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sorting/merge_sort.h"

int search(int* nums,  int numSize, int target){
	//Write your code here....
	//If found return the index
	//Else return -1
	
	return 2;//Trial
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
