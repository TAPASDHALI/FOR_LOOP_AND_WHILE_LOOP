## WRITE FOR LOOP AND WHILE LOOP STATEMENT TO PRINT THE FOLLOWING SERIES:
## 105, 98, 91, .... 7
# start = int(input("Enter any Number: "))
start = 105
step = -7
stop = 7
for i in range(start, stop - 1, step):
    print(i, end=" ")

print()
## while loop
n = int(input("Enter any Number: "))
stop = 7
while n >= stop:
    print(n, end=" ")
    n -= 7