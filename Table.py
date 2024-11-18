m = int(input("Input number of rows: "))
n = int(input("Input number of columns: "))
table = []
sum = 0
# Initialize table
for row in range(m):
    a = []
    for column in range(n):
        a.append(0)
    table.append(a)

# Print table
print("This is the initial table")
for row in range(m):
    for column in range(n):
        print(table[row][column], end=" ")
    print()

# Fill cells with 1
for row in range(m):
    for column in range(n):
        table[row][column] = 1

# Print table with 1
print("This is the table changed to 1")
for row in range(m):
    for column in range(n):
        print(table[row][column], end=" ")
    print()

# Checkerboard pattern from table with 1
for row in range(m):
    for column in range(n):
        if ((row % 2 != 0) and (column % 2 == 0)) or ((row % 2 == 0) and (column % 2 != 0)):
            table[row][column] = 0

# Print checkerboard table
print("This is the checkerboard pattern table")
for row in range(m):
    for column in range(n):
        print(table[row][column], end=" ")
    print()

# Changing top and bottom layers
for row in range(m):
    for column in range(n):
        if row == 0 or row == m-1:
            table[row][column] = 0

# Print top and bottom layer changed
print("This is the table with the top and bottom layer changes")
for row in range(m):
    for column in range(n):
        print(table[row][column], end=" ")
    print()

# Changing left and right columns
for row in range(m):
    for column in range(n):
        if column == 0 or column == n-1:
            table[row][column] = 1

# Print sides changed
print("This is the table with the sides changed")
for row in range(m):
    for column in range(n):
        print(table[row][column], end=" ")
    print()

# Add the elements
for row in range(m):
    for column in range(n):
        sum += table[row][column]

# Print sum
print(f"Adding every element equals to: {sum}")