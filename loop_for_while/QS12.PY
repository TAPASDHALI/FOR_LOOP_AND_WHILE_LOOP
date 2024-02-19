## WAP TO FIND THE SUM OF THE DIGITS OF A NUMBER ACCEPTED FROM THE USER WHILE LOOP:--
## example :-  2345
## 2 + 3 + 4 + 5 = 14

num = int(input("Enter any number:- "))

res = 0
sum = 0
while num > 0:
    res = num % 10
    sum = sum + res
    num = num // 10
print(f'Sum of tje Digits are: {sum}')


print()
## USE FOR LOOP
num = input("Enter any Number:- ")
sum = 0
for i in range(0,len(num)):
    sum = sum + int(num[i])
print("sum of the digits are:- ", sum)