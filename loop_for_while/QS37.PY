## WAP TO FIND THE SUM OF FOLLOWING SERIES?
## 1 + 8 + 27 + .... + N TERMS

n = int(input("Enter the terms of the series from user: "))

sum1 = 0
for i in range(1, n + 1):
    sum1 = sum1 + (i**3)
print(f'Sum of the series: {sum1}')

print()
## while loop
n2 = int(input("Enter the terms of the series from user: "))

sum2 = 0
i = 1
while i <= n2:
    sum2 += (i**3)
    i += 1
print(f'Sum of the series: {sum2}')