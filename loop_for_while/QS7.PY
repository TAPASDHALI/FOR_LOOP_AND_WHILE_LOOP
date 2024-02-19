## WAP TO PRINT SUM OF FIRST 10 NATURAL NUMBERS USE FOR LOOP AND WHILE LOOP:- 
n = int(input("Enter any Number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

print()
## while loop
n = int(input("Enter any Number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)