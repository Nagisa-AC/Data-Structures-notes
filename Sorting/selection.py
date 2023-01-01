def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i  
		for j in range(i+1, len(arr)):
			if arr[min_index] > arr[j]:
				arr[min_index], arr[j] = arr[j], arr[min_index]
	return arr


arr = [15, 28, 17, 12, 18, 9, 6]
arr1 = [23, 4, 12, 30, 2, 0,5]
arr2 = [43, 54, 43, -1100, -100, 3]
arr3 = [float('inf'), float('-inf'), 100, 0, 20]


'''
	Selection sort: Use one pointer (a) to iterate 
	through the array. Keep another pointer (b) to iterate 
	through the all of the elements past 'b'. Check if the 
	value at index 'a' is greater than value at index 'b'.
	If so, swap. 

	Time Complexity: O(N^2) ==> We have one pointer iterating 
	all elements of the array, then another pointer iterating 
	through all of the elemente of the array minus 1. Our time
	complexity is O(N^2) - 1 ==> O(N^2)

	Space Complexity: O(1) ==> No auxilliary space is used  

'''