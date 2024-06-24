''' Timing analysis of Sudoku Puzzles '''
''' The code is implemented in two ways. One using numpy, and other without using numpy arrays.  '''

# Importing the required libraries
import numpy as np
import time
import csv
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sudoku_solver import SudokuSolver,SudokuSolver_NumPy

# Extracting the puzzles from the csv file
file = open('sudoku-15.csv','r')
file = csv.reader(file)

puzzles1 = [[0 for _ in range(81)] for _ in range(15)]
puzzles2 = np.zeros((15,81),dtype=int)
for puzzle in file:
    string = puzzle[1]
    index = int(puzzle[0]) - 1
    puzzles1[index] = list(map(int,string.replace('.','0')))
    puzzles2[index] = np.array(list(map(int,string.replace('.','0'))))

num_puzzles = 15

solver1 = SudokuSolver() # Without NumPy
solver2 = SudokuSolver_NumPy() # With NumPy

solutions1 = [0 for _ in range(num_puzzles)] # List to store whether the input puzzle has solution or not (without numpy)
solutions2 = np.zeros((num_puzzles,),dtype=int) # Array to store whether the input puzzle has solution or not (with numpy)

times1 = [0 for _ in range(num_puzzles)] # List to store the time required to solve each puzzle(without numpy)
times2 = np.zeros((num_puzzles,)) # Array to store the time required to solve each puzzle(with numpy)


table = PrettyTable()
table.field_names = ["Puzzle/Time(s)","Without NumPy","With NumPy"]

# Writing the solutions of the puzzles in to the solutions.txt file
sol_file = open('solutions.txt','w+')

for i in range(num_puzzles):
    start1 = time.time()
    puzzles1[i] = solver1.transform(puzzles1[i],9,9)
    solutions1[i] = solver1.solve(puzzles1[i])
    end1 = time.time()
    start2 = time.time()
    solutions2[i] = solver2.solve(puzzles2[i])
    end2 = time.time()
    print(f"Puzzle {i+1}: Status1: {int(solutions1[i])} | Status2: {solutions2[i]}")
    table.add_row([i+1,end1-start1,end2-start2])
    sol = "".join(list(map(str,puzzles2[i])))
    sol_file.write(sol+"\n")
    times1[i] = end1 - start1
    times2[i] = end2 - start2

print(table)

# Plot between time required and puzzle number
plt.figure(0)
plt.plot(list(range(1,num_puzzles+1)),times1,ms=5,marker='o',label="Without NumPy")
plt.plot(list(range(1,num_puzzles+1)),times2,ms=5,marker='o',label="With NumPy")
plt.xlabel("Puzzle")
plt.ylabel("Time taken(s)")
plt.legend()
plt.show()
