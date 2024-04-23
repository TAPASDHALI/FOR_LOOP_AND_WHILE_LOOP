### WAP TO CHECK ANY NUMBER WHETHER IT IS A PREFECT NUMBER OR NOT?
## PERFECT NUMBER: EXAMPLE:-  28 = 1, 2, 4, 7, 14 
## EXAMPLE:- 1 + 2 + 4 + 7 + 14 = 28
## 6, 28, 496
## USING FOR LOOP
n = int(input("Enter any Number:- "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not a perfect number')

print()
## WHILE LOOP
n2 = int(input("Enter any Number:- "))
sum2 = 0
i2 = 1
while i2 < n2:
    if n2 % i2 == 0:
        sum2 = sum2 + i2
    i2 += 1
if n2 == sum2:
    print(f'{n2} is a perfect numer')
else:
    print(f'{n2} is not a perfect number')