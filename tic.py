import time
grid = [[3 ,1, 6, 5, 7, 8 ,4 ,9, 2],
           [5, 2, 0, 1, 3, 4, 7, 6, 8, ],
           [4, 8, 7, 6, 2, 9, 5, 3, 1 ],
           [2, 6, 3, 4, 0, 5, 9, 8, 7 ],
           [9, 7, 4, 8, 6, 3, 1, 2, 5 ],
           [8, 0, 1, 7, 9, 2, 6, 4, 3 ],
           [1, 3, 8, 9, 4, 7, 2, 5, 6 ],
           [6, 9, 2, 3, 5, 1, 8, 7, 4 ],
           [7, 4, 5, 2, 8, 6, 3, 1, 9,]]

gridcopy = [[3 ,1, 6, 5, 7, 8 ,4 ,9, 2],
           [5, 2, 0, 1, 3, 4, 7, 6, 8, ],
           [4, 8, 7, 6, 2, 9, 5, 3, 1 ],
           [2, 6, 3, 4, 0, 5, 9, 8, 7 ],
           [9, 7, 4, 8, 6, 3, 1, 2, 5 ],
           [8, 0, 1, 7, 9, 2, 6, 4, 3 ],
           [1, 3, 8, 9, 4, 7, 2, 5, 6 ],
           [6, 9, 2, 3, 5, 1, 8, 7, 4 ],
           [7, 4, 5, 2, 8, 6, 3, 1, 9,]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True

            bo[row][col] = 0

    return False
def solve_Bool(bo:list):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None
print_board(grid)
print(solve_Bool(gridcopy))
print_board(grid)