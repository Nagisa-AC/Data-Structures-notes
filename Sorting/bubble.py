def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(0, len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j],arr[j + 1] = arr[j + 1], arr[j]
	return arr 


arr = [15, 28, 17, 12, 18, 9, 6]
arr1 = [23, 4, 12, 30, 2, 0,5]
arr2 = [43, 54, 43, -1100, -100, 3]
arr3 = [float('inf'), float('-inf'), 100, 0, 20]


'''
	bubble sort: think of a bubble that encapsulates
	two elements of the array. Those values are compared.
	ex. arr[i] > arr[i + 1].
	If the above condition is true, swap values. This 
	continues until the largest element of the array is 
	found and placed in arr[len(arr) - 1]

'''