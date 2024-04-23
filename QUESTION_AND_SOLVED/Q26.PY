## WAP TO FIND OF THE NUMBER IS NEON NUMBER OR NOT?

## EXAMPLE = 9 = 9 * 9 = 81
## SUM = 8 + 1 = 9
n = int(input("Enter any Number:- "))
sqr = n * n
sum = 0
temp = sqr
while temp>0:
    rem = temp % 10
    sum = sum + rem
    temp //= 10
if n == sum:
    print(f'{n} is Neon Number')
else:
    print(f'{n} is not a Neon Number')