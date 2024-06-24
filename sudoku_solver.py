''' Sudoku Solver '''

# Importing numpy to make the calulations efficient
import numpy as np

''' Class for Sudoku Solver '''
class SudokuSolver_NumPy:
    
    ''' Check whether the given val is safe at the specified row and col '''
    def is_safe(self,grid,row,col,val):
        # Row wise check
        vertical_check = not (np.count_nonzero(grid[:,col] == val))
        # Column wise check
        horizontal_check = not (np.count_nonzero(grid[row,:] == val))
        # 3x3 box wise check
        start_row = row - (row % 3)
        start_col = col - (col % 3)
        box_check = not (np.count_nonzero(grid[start_row:start_row+3,start_col:start_col+3] == val))
        return vertical_check and horizontal_check and box_check

    ''' It returns the indices of the empty places, if it doesn't find any empty place, it returns False '''
    def find_empty(self,grid,rc):
        for i in range(9):
            zero_indices = np.where(grid[i] == 0)[0]
            if len(zero_indices) > 0:
                rc[0] = i
                rc[1] = zero_indices[0]
                return True
        return False

    ''' It solves the puzzle using Back Tracking Technique '''
    def solve(self,grid):
        grid = grid.reshape((9,9))
        rc = np.zeros((2,),dtype=int) # Array to store the empty place location
        if not self.find_empty(grid,rc):
            return True

        row,col = rc # Assigning the row,col to the empty place

        # Considers digits from 1 to 9
        for val in range(1,10):
            # If the value is safe at the desired location
            if self.is_safe(grid,row,col,val):
                # It assigns the value and perform recursion
                grid[row][col] = val

                if self.solve(grid):
                    return True
                grid[row][col] = 0 # If the val doesn't fit, the value at row,col is assigned to zero again

        # If the puzzle remain unsolved, it returns False
        return False

class SudokuSolver:

    ''' Returns a 2D List of dimensions m x n '''
    def transform(self,grid,m,n):
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(grid)):
            temp[int(i / m)][i % n] = grid[i]
        return temp

    ''' Check whether the given val is safe at the specified row and col '''
    def is_safe(self,grid,row,col,val):
        # Row wise check
        for i in range(9):
            if grid[row][i] == val:
                return False
        # Column wise check
        for j in range(9):
            if grid[j][col] == val:
                return False
        # Box wise check
        start_row = row - (row % 3)
        start_col = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == val:
                    return False
        return True

    ''' It returns the indices of the empty places, if it doesn't find any empty place, it returns False '''
    def find_empty(self,grid,rc):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    rc[0] = i
                    rc[1] = j
                    return True
        return False

    ''' It solves the puzzle using Back Tracking Technique '''
    def solve(self,grid):
        rc = [0,0] # List to store the empty place location
        if not self.find_empty(grid,rc):
            return True

        row,col = rc # Assigning the row,col to the empty place

        # Considers digits from 1 to 9
        for val in range(1,10):
            # If the value is safe at the desired location
            if self.is_safe(grid,row,col,val):
                # It assigns the value and perform recursion
                grid[row][col] = val

                if self.solve(grid):
                    return True
                grid[row][col] = 0 # If the val doesn't fit, the value at row,col is assigned to zero again

        # If the puzzle remain unsolved, it returns False
        return False
