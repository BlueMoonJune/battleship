#! /bin/python3.12
import math

import random

w = int(input("width of grid"))
h = int(input("height of grid"))
shipc = int(input("how many ships"))

# the "ocean"
board = [["O"] * w for _ in range(0, h)]

# prints a 2D array nicely
def print2D(arr):
    for row in arr:
        for cell in row:
            print(cell, end=" ")
        print("")

ship_pos = [(random.randint(0, w), random.randint(0, h)) for _ in range(0, shipc)]

misses = int(math.sqrt(w*h))

# this will keep re-printing the "Ocean" every turn
# untill the user gives a certain input
while True:
    print2D(board)
    user = input("Where would you like to hit? [x, y]")
    x = int(user[:user.find(",")])
    y = int(user[user.find(" ") + 1:])
    if 0 > x >= w or 0 > y >= h:
        print("outside of board")
    elif (x, y) in ship_pos:
        print("You hit a ship!")
        board[y][x] = "@"
        ship_pos.remove((x, y))
        if len(ship_pos) <= 0:
            print("All ships sunk, you win!")
            break
    elif "stop" == user:
        break
    else:
        print("Miss! try again.")
        board[y][x] = "X"
        misses -= 1
        if misses == 0:
            print("You lost, try again")
            break

