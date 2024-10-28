# the "ocean"
board = [["O"] * 5] * 5

# prints a 2D array nicely
def print2D(arr):
    for row in arr:
        for cell in row:
            print(cell, end=" ")
        print("")

print2D(board)
