## WAP TO CHECK IF A NUMBER IS PERFECT SQUARE OR NOT? FROM USER
n = int(input("Enter any number:- "))
f = 0
for i in range(1, n):
    if i * i == n:
        f = 1
        break
if f == 1:
    print(f'{n} is a perfect square number')
else:
    print(f'{n} is not a perfect square number')


print()
## WHILE LOOP
n2 = int(input("Enter any number:- "))
f2 = 0
i2 = 1
while i2 < n2:
    if i2 * i2 == n2:
        f2 = 1
        break
    i2 += 1

if f2 == 1:
    print(f'{n2} is a perfect square number')
else:
    print(f'{n2} is not a perfect squeare numner')

print()
# ## WAP TO PRINT ALL THE PERFECT SQUARE NUMBER IN THE GIVEN RANGE?
# start = int(input("Enter any Number:- "))
# end = int(input("Enter the ending number:- "))
# for n4 in range(start, end + 1):
#     sum = 0
#     for var in range(1, n4):
#         if n4 % var == 0:
#             sum += var
# if sum == n4:
#     print(n4)
