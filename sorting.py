

# selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# test cases 
# test case 1
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
# Expected output: [11, 12, 22, 25, 64]
print(arr)

# test case 2
arr = [5, 2, 1, 3, 4]
selection_sort(arr)
# Expected output: [1, 2, 3, 4, 5]
print(arr)

# bubble sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if swapped == False:
            break
    return arr

# test cases
# test case 1
arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
# Expected output: [11, 12, 22, 25, 64]
print(arr)

# test case 2
arr = [5, 2, 1, 3, 4]
bubble_sort(arr)
# Expected output: [1, 2, 3, 4, 5]
print(arr)
