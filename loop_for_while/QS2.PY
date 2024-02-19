## WAP TO PRINT THE FOLLOWING USING WHILE LOOP?

## A> FIRST 10 EVEN NUMBERS
n = int(input("Enter any number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()
## while loop
n1 = int(input("Enter any Number: "))
even = 1
while even <= n1:
    if even % 2 == 0:
        print(even, end=" ")
    even += 1

print()
## B> FIRST 10 NATURAL NUMBERS
n = int(input("Enter any Number: "))
for i in range(1, n + 1):
    print(i, end=" ")

print()
## while loop
n1 = int(input("Enter any Number: "))
i = 1
while i <= n1:
    print(i, end=" ")
    i += 1

print()
## C> FIRST 10 ORD NUMBER
n = int(input("Enter any Number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

print()
## while loop
n1 = int(input("Enter any Number: "))
i = 1
while i <= n1:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

print()
## D> FIRST 10 WHOLE NUMBERS
n = int(input("Enter any Number: "))
for i in range(0, n + 1):
    print(i, end=" ")

print()
##while loop
n1 = int(input("Enter any Number: "))
i = 0
while i <= n1:
    print(i, end=" ")
    i += 1

