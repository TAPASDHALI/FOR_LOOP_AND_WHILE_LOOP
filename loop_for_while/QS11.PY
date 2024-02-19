## WAP TO CHECK WHETHER A NUMBER IS PRIME OR NOT USING WHILE LOOP?
# num = int(input("Enter any Number:- "))

n1 = int(input("Enter any Number: "))

count1 = 0
for i in range(1, n1+1):
    if n1 % i == 0:
        count1 += 1

if count1 == 2:
    print(f'{n1} is a Prime Number')
else:
    print(f'{n1} is not a Prime Number')



## while loop
print()
n = int(input("Enter any Number:- "))

count = 0
i = 1
while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 2:
    print(f'{n} is a Prime Number')
else:
    print(f'{n} is not a Prime number')
