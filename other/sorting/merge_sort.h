//merge_sort.h

#ifndef __MERGESORT__
#define __MERGESORT__

#include <stdio.h>
#include <stdlib.h>

static void merge(int* arr, int left, int mid, int right);

// static void mergesort(int* arr, int left,  int right);

void sort(int* nums, int numSize);

#endif