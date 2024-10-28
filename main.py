# the "ocean"
board = [["O"] * 5] * 5

# prints a 2D array nicely
def print2D(arr):
    for row in arr:
        for cell in row:
            print(cell, end=" ")
        print("")

# this will keep re-printing the "Ocean" every turn
# untill the user gives a certain input
while True:
    print2D(board)
    user = input("Where would you like to hit?")
    if "stop" in user:
        break

