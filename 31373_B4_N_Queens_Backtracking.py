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

# Main Program
print("\n     N-Queens Problem")
N = int(input("\nEnter the side of board (N) : "))
board = [['_' for _ in range(N)] for _ in range(N)]

B = Backtrack(N)
if B.solve(board, 0, 0):
    print("\nSolution exists!!\n")
    for i in range(N):
        print(*board[i],"\n")
else:
    print("\nNo solution exists!!")
