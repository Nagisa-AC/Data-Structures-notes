'''
    Selection Sort: Sorting algo

    - iterate through array looking for min_val 
    - shift min_val to smallest available index (SAI)
    - pointer to keep track of SAI 
    Time: O(N^2)
    Space: O(1)
'''

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i 
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                arr[j],arr[min_index] = arr[min_index],arr[j]
    print(arr)




def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]
    print(arr) 



'''
    Bubble sort: Sorting algo
    - processing 2 elements at the same time: arr[i], arr[j]
    - Checking if arr[i] > arr[j]
    - If above == true ==> swap 
    - At every iterating ==> greatests element shifting right
'''



# selectionSort([3,4,5,1,0,2])
# selectionSort([9,8,7,6,5,4,3,2,1])
bubbleSort([3,4,5,1,0,2])
bubbleSort([9,8,7,6,5,4,3,2,1])