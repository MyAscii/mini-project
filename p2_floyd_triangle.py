row = int(input("How many rows :"))
num = 1
for x in range(row):
    for y in range(x+1):
        print(num, end = " ")
        num = num + 1
    print()