## WAP TO CHECK WHETHER A NUMBER IS ARMSTRONG OR NOT.
## (ARMSTRONG NUMBER IS A NUMBER THAT EQUAL TO THE SUM OF CUBES OF ITS DIGITS
## FOR EXAMPLE:- 153 = 1^3 + 5^3 + 3^3)
## FOR EXAMPLE:- 663 = 6^3 + 6^3 + 3^3
## FOR EXAMPLE:- 407 = 4^3 + 0^3 + 7^3

## list of the armstrong number:- 1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474,54748,92727,93084,548834,1741725,4210818


num = int(input("Enter any Number:- "))
sum = 0
temp = num
while temp > 0:
    digits = temp % 10
    quabe = digits ** 3
    sum = sum + quabe
    temp //= 10
if num == sum:
    print(f'{sum} is a Armstrong Number')
else:
    print(f'{num} is not a Armstrong Number')

print()
## for loop
n1 = int(input("Enter any Number: "))
sum1 = 0
temp1 = n1
for i in range(1, temp1 + 1):
    digits = temp1 % 10
    quable = digits ** 3
    sum1 += quable
    temp1 //= 10
if sum1 == n1:
    print(f'{sum1} is a Armstrong Number: ')
else:
    print(f'{n1} is Not a Armstrong')


print()
## user defind digits
num1 = input("Enter any number:- ")
digit_sum = 0
for i in num1:
    digit_sum = digit_sum + int(i) ** len(num1)
if int(num1) == digit_sum:
    print(num1, "is an Armstrong Number")
else:
    print(num1, "is not a Armstrong Number")