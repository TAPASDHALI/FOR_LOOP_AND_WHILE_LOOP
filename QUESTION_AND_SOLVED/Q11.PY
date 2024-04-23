## WAP TO DISPLAY SUM OF EVEN NUMBER UP TO THE NUMBER ENTERED BY THE USER?
## USING FOR LOOP
n = int(input("Enter any number:- "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)

print()
## USING WHILE LOOP
n2 = int(input("Enter any Number:- "))
sum2 = 0
j = 0
while j <= n2:
    if j % 2 == 0:
        sum2 = sum2 + j
    j += 1
print(sum2)

print()
## WAP TO DISPLAY SUM OF ODD NUMBER UP TO THE NUMBER ENTERED BY USER
## USING FOR LOOP
n3 = int(input("Enter any Number:- "))
sum3 = 0
for i2 in range(1, n3 + 1):
    if i2 % 2 != 0:
        sum3 = sum3 + i2
print(sum3)


print()
## WAP TO DISPLAY SUM OF ODD NUMBER UP TO THE NUMBER ENTERED BY USER
## USING FOR LOOP
n4 = int(input("Enter any Number:- "))
sum4 = 0
j2 = 1
while j2 <= n4:
    if j2 % 2 != 0:
        sum4 = sum4 + j2
    j2 += 1
print(sum4)