number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# print the whole first row
print(number_grid[0])

# print the first element of the first nested list
print(number_grid[0][0])

# print another specific element 
print(number_grid[2][1])

# print the whole nested list in a row
print(number_grid)

# another way to print the whole nested list
for row in number_grid:
    print(row)

# print every element separatly
for row in number_grid:
    for col in row:
        print(col)    