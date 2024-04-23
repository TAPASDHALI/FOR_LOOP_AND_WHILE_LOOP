## WAP TO CHECK INPUTED NUMBER IS PRIME NUMBER OR NOT?
## EXAMPLE:- 3, 5, 7, 11, 13, 17, 19
n = int(input("Enter the Number:- "))
count = 0
for i in range(2, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print(f'{n} is not a Prime Number')
else:
    print(f'{n} is a prime number')
