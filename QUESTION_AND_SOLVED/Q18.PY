## WAP TO CHECK INPUTED NUMBER IS A PRIME NUMBER OR NOT?
## EXAMPLE:- 3, 5, 7, 11, 13 17, 19, 23, 29, 31, 37, 41, 47 ECT
##while loop
n = int(input("Enter any number:- "))

count = 0
i = 1
while i <= n:
    if n % i == 0:
        count = count + 1
    i += 1
if (count == 2):
    print('prime number')
else:
    print('not prime number')


print()
## FOR LOOP
n2 = int(input("Enter any Number:- "))
count2 = 0
for var in range(n2 - 1, 2):
    if n2 % var == 0:
        count2 = count2 + 1
if count2 == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")