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
print(max_subarray_sum([1, 2, 3, 4, -1, -2, 5, 6]))  # 18
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray_sum([-2, -3, -4, -1, -2, -1, -5, -3]))  # -1
print(max_subarray_sum([1, 2, 3, 4, -1, -2, 5, 6]))  # 18
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(max_subarray_sum([-2, -3, -4, -1, -2, -1, -5, -3]))  # -1


# Time complexity: O(n) 
# Space complexity: O(1) 

 
