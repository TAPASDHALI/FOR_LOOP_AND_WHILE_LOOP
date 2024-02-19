## WAP TO FIND THE SUM OF FOLLOWING SERIES:
## 1 + 2 + 6 + 24 + 120 + 720 + .... + N TERMS?

n = int(input("Enter the term of the series from user: "))

sum1 = 0
stor = 1
for i in range(1, n + 1):
    stor = stor * i
    sum1 += stor
print(sum1)

print()
## WHILE LOOP

n2 = int(input("Enter the term of the series from user: "))
sum2 = 0
stor2 = 1
i = 1
while i <= n2:
    stor2 = stor2 * i
    sum2 += stor2
    i += 1
print(f'Sum of the series term: {sum2}') 