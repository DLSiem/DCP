"""
Given a marrix of size m x n, find the transpose of the matrix.
"""

def transpose_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # transposed_matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# Test cases
print("\n\n---Test cases for transpose_matrix---")

print("__Test case 1__")
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nBefore transpose:")
for i in mat1:
    print(i)

print("\nAfter transpose:")
for i in transpose_matrix(mat1):
    print(i)
 

print("__Test case 2__")
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("\nBefore transpose:")
for i in mat2:
    print(i)

print("\nAfter transpose:")
for i in transpose_matrix(mat2):
    print(i)

# Time complexity: O(n * m)
# Space complexity: O(1) 
    







# """
# Given a square matrix, rotate the matrix by 90 degrees in an anti-clockwise direction.
# """

# def rotate_matrix(matrix):
#     n = len
#     matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix

# # Test cases
# print("\n\n---Test cases for rotate_matrix---")
# print([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

# print([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# print(rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))  # [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]

# # Time complexity: O(n^2)
# # Space complexity: O(1)

 