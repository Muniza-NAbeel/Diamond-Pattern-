# Number of rows for the upper half (including the middle row)
rows = 5

# Print the upper pyramid
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Print the lower inverted pyramid
for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
