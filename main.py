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
    vert = input("Where would you like to hit verticaly? from botom to top 1 to 5.")
    horo = input("Where would you like to hit horozontly? from left to tright 1 to 5.")
    user = (vert, horo)
    if user == ship_pos:
        print("Hit! you win!")
    elif "stop" in vert or horo:
        break
    else:
        print("Wrong! try again.")
