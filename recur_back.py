"""
Factorial of a number using recursion
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test cases
print("\n---Test cases for factorial---")
print(factorial(5))  # 120
print(factorial(4))  # 24
print(factorial(3))  # 6
print(factorial(2))  # 2

# Time complexity: O(n) since the function is called n times
# Space complexity: O(n) since the function is called n times

"""
tower of hanoi
You are given three rods (numbered 1 to 3), and ‘N’ disks initially placed on the first rod, one on top of each other in increasing order of size ( the largest disk is at the bottom). You are supposed to move the ‘N’ disks to another rod(either rod 2 or rod 3) using the following rules and in less than 2 ^ (N) moves.

1. You can only move one disk in one move. 
2. You can not place a larger disk on top of a smaller disk.
3. You can only move the disk at the top of any rod.
"""

def towerOfHanoi(n):

    def move(n, source, target, auxiliary, moves):
        if n == 1:
            moves.append((source, target))
            return
        move(n -1, source, auxiliary, target, moves)
        moves.append((source, target))
        move(n - 1, auxiliary, target, source, moves)

    moves = []
    move(n, 1, 3, 2, moves)
    return moves

# Test cases
print("\n---Test cases for towerOfHanoi---")
print(towerOfHanoi(2))  # [(1, 2), (1, 3), (2, 3)]
print(towerOfHanoi(3))  # [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)]

