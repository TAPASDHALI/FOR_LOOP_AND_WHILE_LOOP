## WAP TO PRINT TABLE ANY NUMBERS?
num = int(input("Enter The Table number:- "))
table = 10
for i in range(1, table + 1):
    print(num, "*", i, "=", num * i)

print()
## WAP TO FIND FIRST N MULTIPLES OF A NUMBERS?
## USING FOR LOOP AND WHILE LOOP
n = int(input("Enter any number:- "))
for i in range(1, n + 1):
    res = n * i
    print(res, end=" ")

print()
## WHILE LOOP
n2 = int(input("Enter any Number:- "))
j = 1
res2 = 0
while j <= n2:
    res2 = n2 * j
    j += 1
    print(res2, end=" ")
