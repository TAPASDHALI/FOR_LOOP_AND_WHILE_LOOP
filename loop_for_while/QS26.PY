## WAP TO SUM OF SEQUENCY?
## 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

n = int(input("Enter any Number: "))
f = 1
sum = 0
for i in range(1, n + 1):
    f = f * i
    sum += 1/f
print(sum)

print()
n1 = int(input("Enter any Number:- "))
f1 = 1
sum1 = 0
i = 1
while (i <= n1):
    f1 = f1 * i
    sum1 = sum1 + 1/f1
    i += 1
print(sum1)