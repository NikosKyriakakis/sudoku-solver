import math
import sys


grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_sudoku():
    global grid

    column = 0
    row = 0   
    print("-------------------------------") 
    for i in range(9):
        print("|", end="")
        for j in range(9):
            if grid[i][j] == 0:
                print(" {} ".format("-"), end="")
            else:
                print(" {} ".format(grid[i][j]), end="")
            column += 1
            if column == 3:
                column = 0
                print("|", end="")
        row += 1
        print("")
        if row == 3:
            row = 0
            print("-------------------------------")


def is_move_possible(x, y, n):
    global grid
    
    for j in range(9):
        if grid[j][y] == n:
            return False
        if grid[x][j] == n:
            return False
    xs = (x // 3) * 3
    ys = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[i + xs][j + ys] == n:
                return False
    return True             


def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if is_move_possible(i, j, n):
                       grid[i][j] = n
                       solve()
                       grid[i][j] = 0
                return
    print_sudoku()
    sys.exit(0)
    

def main():
    print_sudoku()
    input("Press ENTER to proceed to solution: ")
    solve()    

    
main()
