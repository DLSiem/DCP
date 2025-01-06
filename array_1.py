"""
# Kidane's Algorithm
1. Given an array of integers (both positive and negative), find the contiguous subarray that has the largest sum and return the sum of that subarray.
"""

def max_subarray_sum(arr):
    max_sum = float('-inf') # Initialize the max sum to negative infinity.
    current_sum = 0 # Initialize the current sum to 0.

    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i]) # If the current element is greater than the sum of the current element and the previous sum, then the current element is the new sum.

        max_sum = max(max_sum, current_sum) # If the current sum is greater than the max sum, then the current sum is the new max sum.

    return max_sum

# Test cases
print("\n---Test cases for max_subarray_sum---")
print(max_subarray_sum([1, 2, 3, 4, -1, -2, 5, 6]))  # 18
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray_sum([-2, -3, -4, -1, -2, -1, -5, -3]))  # -1
print(max_subarray_sum([1, 2, 3, 4, -1, -2, 5, 6]))  # 18
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray_sum([-2, -3, -4, -1, -2, -1, -5, -3]))  # -1



# Time complexity: O(n) 
# Space complexity: O(1) 


"""2. Given an array consisting of three distinct values (e.g., 0, 1, 2), rearrange the array such that all instances of:

    The first value (e.g., 0) appear at the beginning.
    The second value (e.g., 1) appear in the middle.
    The third value (e.g., 2) appear at the end.
 """

def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if mid == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif mid == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Test cases
print("\n\n---Test cases for sort_array---")
print(sort_array([0, 1, 2, 0, 1, 2]))  # [0, 0, 1, 1, 2, 2]
print(sort_array([2, 1, 0, 2, 1, 0]))  # [0, 0, 1, 1, 2, 2]
print(sort_array([2, 1, 0, 0, 1, 2]))  # [0, 0, 1, 1, 2, 2]
print(sort_array([2, 1, 0, 0, 1, 2]))  # [0, 0, 1, 1, 2, 2]
print(sort_array([0, 1, 2, 0, 1, 2]))  # [0, 0, 1, 1, 2, 2]
