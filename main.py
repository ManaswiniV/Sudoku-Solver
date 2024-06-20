''' Timing analysis of Sudoku Puzzles '''

# Importing the required libraries
import numpy as np
import time
import csv
import matplotlib.pyplot as plt
from sudoku_solver import SudokuSolver

# Extracting the puzzles from the csv file
file = open('Sudoku_Solver\sudoku-15.csv','r')
file = csv.reader(file)
puzzles = np.zeros((15,81),dtype=int)
for puzzle in file:
    string = puzzle[1]
    index = int(puzzle[0]) - 1
    puzzles[index] = np.array(list(map(int,string.replace('.','0'))))

num_puzzles = len(puzzles)

solver = SudokuSolver()

solutions = np.zeros((num_puzzles,),dtype=int) # Array to store whether the input puzzle has solution or not
times = np.zeros((num_puzzles,)) # Array to store the time required to solve each puzzle

# Solver
for i in range(num_puzzles):
    start = time.time()
    solutions[i] = solver.solve(puzzles[i])
    end = time.time()
    print(f"Time taken to solve Puzzle({i+1}):",end-start)
    times[i] = end - start

# Writing the solutions of the puzzles in to the solutions.txt file
sol_file = open('Sudoku_Solver\solutions.txt','w+')
for i in range(num_puzzles):
    sol = "".join(list(map(str,puzzles[i])))
    sol_file.write(sol+"\n")

# Plot between time required and puzzle number
plt.figure(0)
plt.plot(list(range(1,num_puzzles+1)),times,ms=5,marker='o')
plt.xlabel("Puzzle")
plt.ylabel("Time taken")
plt.title(f"Total time required to solve {num_puzzles} puzzles: {np.sum(times)}s")
plt.show()