## WRITE FOR LOOP STATEMENT TO PRINT THE FOLLOWING SERIES
## 10, 20, 30 ...  ...  300

## for loop
n = int(input("Enter any Number: "))
for i in range(1, n+1):
    if i % 10 == 0:
        print(i, end=" ")

print()
## while loop
n1 = int(input("Enter any Number: "))
i = 1
while i <= n1:
    if i % 10 == 0:
        print(i, end=" ")
    i += 1