## WAP TO PRINT ALL EVEN NUMBERS THAT FALLS BETWEEN TWO NUMBERS(EXCLUSIVE BOTH NUMBERS) 
## ENTERED FROM THE USER USING WHILE LOOP.

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

if n1 > n2:

    while n1 >= n2:
        if n2 % 2 == 0:
            print(n2, end=" ")
        n2 += 1
else:
    while n2 >= n1:
        if n1 % 2 == 0:
            print(n1, end=" ")
        n1 += 1

print()
## for loop
n3 = int(input("Enter 1st Number: "))
n4 = int(input("Enter 2nd Number: "))

if n3 > n4:
    for i in range(n4, n3 + 1):
        if i % 2 == 0:
            print(i, end=" ")

else:
    for j in range(n3, n4 + 1):
        if j % 2 == 0:
            print(j, end=" ")