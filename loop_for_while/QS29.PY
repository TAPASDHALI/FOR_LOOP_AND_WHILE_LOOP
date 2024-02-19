## WAP TO PRINT ALL ODD NUMBERS THAT FALLS BETWEEN TWO NUMBERS(EXELUSIVE BOTH NUMBERS)
## ENTERED FROM THE USER USING WHILE LOOP
## for loop
n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

if n1 > n2:
    for i in range(n2, n1 +1):
        if i % 2 != 0:
            print(i, end=" ")
else:
    for j in range(n1, n2+1):
        if j % 2 != 0:
            print(j, end=" ")

print()
## while loop
n3 = int(input("Enter 1st Number: "))
n4 = int(input("Enter 2nd Number: "))

if n3 > n4:
    while n3 >= n4:
        if n4 % 2 != 0:
            print(n4, end=" ")
        n4 += 1

else:
    while n4 >= n3:
        if n3 % 2 != 0:
            print(n3, end=" ")
        n3 += 1