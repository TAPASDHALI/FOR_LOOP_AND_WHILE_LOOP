## WAP TO FIND THE NUMBER IS MAGIC NUMBER OR NOT?
## example 289 = 2 + 8 + 9 = 19/ 19 = 1 + 9 = 10
## more example  50113 = 5 + 0 + 1 + 1 + 5 =12 / 12 = 1 + 2 = 3
n = int(input("Enter any Number:- "))
temp = n
while temp > 9:
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum + rem
        temp //= 10
    temp = sum
if sum == 1:
    print(f'{n} is a Magic Number')
else:
    print(f'{n} is not a Magic Number')