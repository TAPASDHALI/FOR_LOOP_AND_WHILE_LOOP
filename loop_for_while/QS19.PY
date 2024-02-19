## WAP TO ADD FIRST N TERMS OF THE FOLLOWING SERIES USING A FOR LOOP?
## 1/1! + 1/2! + 1/3! + ..... + 1/N!

n = int(input("Enter the number of terms to the series:- "))
fac = 1
add = 0
for i in range(1, n+1):
    fac = fac * i
    add += 1/fac
print(add)

## while loop
n1 = int(input("Enter any Number: "))
sum1 = 0
fac1 = 1
i = 1
while n1 > i:
    fac1 = fac * i
    sum1 += 1/fac1
    i += 1
print(sum1)
