def n_queen(n):
    board = [[0]*n for _ in range(n)]
    
    def safe(row, col, board,n):
        
        for i in range(n):
            # check for the colum
            if board[i][col] == 1:
                return False
            if board[row][i] == 1:
                return False


        # check for diagonal from bottom-left to top right
        if row+col<n:
            for i in range(row+col,0,-1):
                if board[i][row+col-i] == 1:
                    return False
        if row+col>=n:
            for i in range(n-1, row+col-n+1,-1):
                if board[i][row+col-i] == 1:
                    return False
        
        # check for diagonal from top-left to bottom right
        if row<=col:
            for i in range(0, n-col+row):
                if board[i][col-row+i] == 1:
                    return False
        if row>col:
            diff = row - col
            for i in range(0, n-diff):
                if board[diff+i][i] == 1:
                    return False
        return True
    
    def solve(col, board, n, solutions):
        # If all queens are placed add to the solution
        if col == n:
            
            solutions.append([row[:] for row in board])
            return
        
        # try putting queen in every row of the current column
        else:
            for i in range(n):
                if safe(i, col,board,n):
                    board[i][col] = 1
                    solve(col+1, board, n, solutions)
                    board[i][col] = 0 # backtrack to try other rows in the current column
                
 
    solutions = []
    solve(0,board,n,solutions)
    
    
    return solutions
        



n = 4
if len(n_queen(n)) == 0:
    print(f"No solution exis for n = {n}.")
else:
    count = 0
    for soln in n_queen(n):
        count += 1
        print(f"Possible solution {count}")
        for row in soln:
            print(row)
        print("------------------\n ")
            
             
        