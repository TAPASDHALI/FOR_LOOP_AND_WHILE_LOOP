## WAP TO PRINT SUM OF FIRST 10 ODD NUMBERS 
n = int(input("Enter any Number: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum += i
print(sum)

print()
## while loop
n1 = int(input("Enter any number: "))
sum = 0
i = 1
while i <= n1:
    if i % 2 != 0:
        sum += i
    i += 1
print(sum)