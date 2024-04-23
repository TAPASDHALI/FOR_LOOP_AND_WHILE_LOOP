## WAP TO CHECK ANY NUMBER WHETHER IT IS AN ARMSTRONG NUMBER OR NOT? THREE DIGITS
## EXAMPLE = 371, 153, 407
## 3 * 3 * 3 = 27
## 7 * 7 * 7 = 343
## 1 * 1 * 1 = 1
## ----------------
##             371

## (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3) = 153
## USING WHILE LOOP
n = int(input("Enter any Three Digits Number:- "))
temp = n
sum = 0
digit = 0
# i = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp //= 10
if n == sum:
    print(f'{n} is an Armstrong Number') 
else:
    print(f'{n} is not a Armstrong Number') 


print()
## USING FOR LOOP
n2 = int(input("Enter any Three Digits Number:- "))
temp2 = n2
sum2 = 0
digit2 = 0
for i in range(1, temp2 + 1):
    digit2 = temp2 % 10
    sum2 = sum2 + digit2 ** 3
    temp2 //= 10
if n2 == sum2:
    print(f'{n2} is an Armstrong Number')
else:
    print(f'{n2} is not an Armstrong Number')



## FOUR DIGITS ARMSTRANGS NUMBER:
n3 = int(input("Enter any DIGITS Number:- "))
count_of_digits = 0
temp = n3
while temp:
    temp //= 10
    count_of_digits += 1
temp = n3
res = 0
while temp:
    last_digit = temp % 10
    res = res + (last_digit ** count_of_digits)
    temp //= 10
if n3 == res:
    print(f'{n3} is an Armstrong Number')
else:
    print(f'{n3} is not an Armstrong Number') 
