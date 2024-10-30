import random

w = 5
h = 5

# the "ocean"
board = [["O"] * w for _ in range(0, h)]

# prints a 2D array nicely
def print2D(arr):
    for row in arr:
        for cell in row:
            print(cell, end=" ")
        print("")

ship_pos = (random.randint(0, w), random.randint(0, h))

misses = 0

# this will keep re-printing the "Ocean" every turn
# untill the user gives a certain input
while True:
    print2D(board)
    user = input("Where would you like to hit horozontly? [x, y]")
    x = int(user[:user.find(",")])
    y = int(user[user.find(" ") + 1:])
    if 0 > x >= w or 0 > y >= h:
        print("outside of board")
    elif (x, y) == ship_pos:
        print("Hit! you win!")
        break
    elif "stop" == user:
        break
    else:
        print("Miss! try again.")
        board[y][x] = "X"
        misses += 1
        if misses == 5:
            print("You lost, try again")
            break

