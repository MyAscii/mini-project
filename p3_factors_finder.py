def factors_finder(x):
    print("The factors of",x,"are :")
    for i in range (1, x + 1):
        if x % i == 0:
            print(i)

y = int(input("What is the number you are trying to find the factor :"))
factors_finder(y)