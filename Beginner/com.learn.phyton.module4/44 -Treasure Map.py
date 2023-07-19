row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure ? \n")
x = [int(a) for a in position]
if len(x) > 2:
    print("Put a valid position")
column = x[0] - 1
row = x[1] - 1
map[row][column] = "X"
print(f"{map[0]}\n{map[1]}\n{map[2]}")
