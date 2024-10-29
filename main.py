import random

w = 5
h = 5

# the "ocean"
board = [["O"] * w] * h

# prints a 2D array nicely
def print2D(arr):
    for row in arr:
        for cell in row:
            print(cell, end=" ")
        print("")

ship_pos = (random.randint(0, w), random.randint(0, h))

# this will keep re-printing the "Ocean" every turn
# untill the user gives a certain input
while True:
    print2D(board)
    user = input("Where would you like to hit?")
    if "stop" in user:
        break

