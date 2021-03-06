from os import system
import time

square = u"\u2588" * 2

width = 30
height = 30
lines = []
offsety = 2
offsetx = 23

for line in lines:
    s = ''.join(line)
    print(s)


def create_new_board():
    lines = []
    for i in range(height):
        lines.append(['. '] * width)
    return lines


def display_board():
    system('cls')
    for line in lines:
        s = ''.join(line)
        print(s)
    time.sleep(0.05)


def find_neighbors(row, col):
    """"""
    n = 0
    # Check the value of the neighbour who is up one row and to the left
    if row > 0 and col > 0 and lines[row - 1][col - 1] == square:
        n += 1
    if row > 0 and lines[row - 1][col] == square:
        n += 1
    if row > 0 and col < width - 1 and lines[row - 1][col + 1] == square:
        n += 1
    if col > 0 and lines[row][col - 1] == square:
        n += 1
    if col < width - 1 and lines[row][col + 1] == square:
        n += 1
    if row < height - 1 and col > 0 and lines[row + 1][col - 1] == square:
        n += 1
    if row < height - 1 and lines[row + 1][col] == square:
        n += 1
    if row < height - 1 and col < width - 1 and lines[row + 1][col + 1] == square:
        n += 1
    return n


def update_board():
    """
    create new empty board
    iterate over all cells
    for each cell find its neighbors
    if neighbors == 2 or 3 then set the current cell in the new board
    return new board
    """
    board = create_new_board()
    # iterate over the row and col indices of each cell and then call find_n...
    for row in range(height):
        for col in range(width):
            n = find_neighbors(row, col)
            if n in (2, 3) and lines[row][col] == square:
                board[row][col] = square
            if lines[row][col] != square and n == 3:
                board[row][col] = square
    return board



def main():
    global lines
    lines = create_new_board()
    # lines[0][0] = square
    # lines[1][0] = square
    # lines[0][1] = square
    # lines[1][1] = square
    lines[1+offsety][3+offsetx] = square
    lines[1+offsety][6+offsetx] = square
    lines[2+offsety][2+offsetx] = square
    lines[3+offsety][2+offsetx] = square
    lines[3+offsety][6+offsetx] = square
    lines[4+offsety][2+offsetx] = square
    lines[4+offsety][3+offsetx] = square
    lines[4+offsety][4+offsetx] = square
    lines[4+offsety][5+offsetx] = square
    while True:
        lines = update_board()
        display_board()


if __name__ == '__main__':
    main()
