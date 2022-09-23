def pascals_triangle(x):
    for i in range(1, x+1):
        for j in range(0, x-i+1):
            print(' ', end='')
 
        C = 1
        for j in range(1, i+1):
 
            print(' ', C, sep='', end='')
 
        # Binomial Coefficient
            C = C * (i - j) // j
        print()

y = int(input("How many rows do you want of the pascals triangle :"))
pascals_triangle(y)