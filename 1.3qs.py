def print_pyramid(rows):
    for i in range(1, rows + 1):
        
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        for l in range(i - 1, 0, -1):
            print(l, end="")
        print()
rows = int(input("Enter the number of rows: "))
print_pyramid(rows)
