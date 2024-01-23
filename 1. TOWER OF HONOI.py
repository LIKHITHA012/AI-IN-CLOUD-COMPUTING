def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# Get user input for the number of disks
while True:
    try:
        N = int(input("Enter the number of disks: "))
        if N > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# A, C, B are the names of rods
TowerOfHanoi(N, 'A', 'C', 'B')


