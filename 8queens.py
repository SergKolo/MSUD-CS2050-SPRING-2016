'''
Create a program that solves the eight queens problems. Briefly stated, the eight queens problem is finding an arrangement of eight queens on an eight by eight chessboard such that all eight are safe from either other. Your solution will need to be recursive.

This method assumes the solution is a list of tuples such as:
[(0, 1), (1, 3), (2, 0), (3, 2)]

For extra credit, have your program solve the problem of any size. For extra-extra create, have you program find all the solutions of a given size; for example, there are 92 solutions for eight queens.
'''
from __future__ import print_function

def print_board(solution):
    length = len(solution)
    print("for:", length)
    print('-' * length)

    if solution == []:
        print("no solution found")
    else:
        for i in range(length):
            for j in range(length):
                if (i, j) in solution:
                    print("Q", end="")
                else:
                    print(".", end="")
            print()

    print('-' * length)

'''
Given the location of two queens, find if they are safe
from each other.
'''
def safe((x1, y1), (x2, y2)):
    if x1 == x2: return False
    if y1 == y2: return False
    if abs(x2-x1) == abs(y2-y1): return False
    return True


def solve_queens(row,queens):
   # if the row > the size of the board, we're done
   if row >= grid_size:
      return True

   for column in range(grid_size):
        if not queens: # we've backtracked or just started
           print("initializing the list:",column,row)
           queens = [(column,row)]
           continue
           
        print("at column,row: ", column,row  )
        safe_spot = True 
        for queen in queens:                 # test against all queen
            if not safe((column,row),queen): # if any of them can attack
               safe_spot = False             # this is not a safe spot
               break                         # 
        if not safe_spot:                    # so advance to the next column
             print("Column ",column,"isn't safe")
             continue                        #
              
        else: # column is safe, so move on to next row
              queens.append((column,row))
              if not solve_queens(row+1,queens): # if we cannot solve next line, backtrack
                  print(">>> cant solve row ",row+1)
                  queens = []
                  continue

        # safe column found , work on next row
        #if not solve_queens(row+1):
        #   queens.pop()
        #   return False

grid_size = 4
queens = [(1,0)]
solve_queens(1,queens)
print(queens)
