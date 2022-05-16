class Backtrack:
    # Constructor
    def __init__(self, n):
        self.N = n
    

    # Function to check if a grid configuration is valid or not
    def is_valid(self, grid, row, col):
        # Note : We only need to check previous columns as queens have already been placed there
        
        # Current row
        for i in range(col):
            if grid[row][i]=='Q':
                return False    
        
        # Diagonal to upper-left
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if grid[i][j]=='Q':
                return False
        
        # Diagonal to bottom-left
        for i,j in zip(range(row,self.N,1),range(col,-1,-1)):
            if grid[i][j]=='Q':
                return False
        
        return True


    # Function to solve the N-queen problem using Backtracking
    def solve(self, grid, col, placed):
        # If all N queens have been provided valid positions
        if placed == len(grid):
            return True
        
        # If all columns have been considered but all queens haven't been placed
        if col == len(grid[0]):
            return False

        # Consider each row for current column (col) and try to place the queen. If not possible then return False
        for r in range(len(grid)):
            if self.is_valid(grid, r, col):
                grid[r][col] = 'Q'
                if self.solve(grid, col+1, placed+1):
                    return True
                grid[r][col] = '_'
        
        return False



class Branch_and_Bound:
    # Constructor
    def __init__(self, n):
        self.N = n
    
    # Function to check if board configuration is valid or not
    def is_valid(self, row, col, fwd_diag, bck_diag, row_check, fwd_diag_check, bck_diag_check):
        if fwd_diag_check[fwd_diag[row][col]]:
            return False
        
        if bck_diag_check[bck_diag[row][col]]:
            return False
        
        if row_check[row]:
            return False
        
        return True

    # Function to solve the N-queen problem using Branch and Bound
    def solve(self, board, col, fwd_diag, bck_diag, row_check, fwd_diag_check, bck_diag_check):
        if(col>=self.N):
            return True

        for row in range(self.N):
            if self.is_valid(row, col, fwd_diag, bck_diag, row_check, fwd_diag_check, bck_diag_check):
                '''
                Place the queen on board[row][col]
                '''
                board[row][col] = 'Q'
                row_check[row] = True
                fwd_diag_check[fwd_diag[row][col]] = True
                bck_diag_check[bck_diag[row][col]] = True

                '''
                Recur to place rest of the queens
                '''
                if self.solve(board, col+1, fwd_diag, bck_diag, row_check, fwd_diag_check, bck_diag_check):
                    return True
                
                '''                
                If placing queen in board[row][col] doesn't lead to a solution,then 
                backtrack (remove queen from board[row][col] and restore checks)
                '''
                board[row][col] = '_'
                row_check[row] = False
                fwd_diag_check[fwd_diag[row][col]] = False
                bck_diag_check[bck_diag[row][col]] = False

        '''
        If queen can't be placed in any row of this column, then return False
        '''    
        return False




# Main Program
print("\n     N-Queens Problem")
N = int(input("\nEnter the side of board (N) : "))
board = [['_' for _ in range(N)] for _ in range(N)]

print("\nAlgorithms to Solve N-Queens Problem")
print("1. Backtracking")
print("2. Branch and Bound")
m = int(input("Enter the algorithm to use (1 or 2) : "))

if m==1:
    B = Backtrack(N)
    if B.solve(board, 0, 0):
        print("\nSolution exists!!\n")
        for i in range(N):
            print(*board[i])
    else:
        print("\nNo solution exists!!")
elif m==2:
    BB = Branch_and_Bound(N)
    fwd_diag = [[i+j for j in range(N)] for i in range(N)]
    bck_diag = [[i-j+(N-1) for j in range(N)] for i in range(N)]

    row_check = [False] * N
    fwd_diag_check = [False] * (2*N-1)
    bck_diag_check = [False] * (2*N-1)
    
    if BB.solve(board, 0, fwd_diag, bck_diag, row_check, fwd_diag_check, bck_diag_check):
        print("\nSolution exists!!\n")
        for i in range(N):
            print(*board[i])
    else:
        print("\nNo solution exists!!")
else:
    print("Wrong Choice!!")
