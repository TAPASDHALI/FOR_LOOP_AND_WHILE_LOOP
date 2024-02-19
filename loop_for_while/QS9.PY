## WAP TO PRINT TABLE OF A NUMBER FROM THE USER.
n = int(input("Enter any Number: "))
n2 = 10
table = 0
for i in range(1 , n2 + 1):
    table = n * i 
    print(n, "*", i, "=", table)

print()
### while loop
n3 = int(input("Enter any Number: "))
n4 = 10
table2 = 0
i = 1
while i <= n4:
    table2 = n3 * i
    print(n3, "*", i, "=", table2)
    i += 1

