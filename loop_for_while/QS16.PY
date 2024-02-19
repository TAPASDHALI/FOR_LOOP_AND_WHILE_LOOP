## WAP TO PRINT THE FIBONACCI SERIES TILL N TERMS(ACCEPT N FROM USER) USING WHILE LOOP:- 

## FIBONACCI SERIES:- 0 1 1 2 3 5 8 13 21 34 55........
# X = 0, Y = 1
## Z = 1

num = int(input("Enter any number:- "))
x = 0
y = 1
z = 0
while z <= num:
    print(z, end=" ")
    x = y
    y = z
    z = x + y

print()
## USE FOR LOOP
num = int(input("Enter any number:- "))
z = 0
y = 1
for x in range(1, num+1):
    print(z, end=" ")
    x = y
    y = z
    z = x + y