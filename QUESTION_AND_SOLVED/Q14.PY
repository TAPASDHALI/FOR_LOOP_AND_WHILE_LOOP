## WAP TO DISPLAY THE FACTORIAL OF AN INPUTED NUMBER FROM USER?
## example :- 5 = 1 * 2 * 3 * 4 * 5 = 120
## more example:- 7 = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040
## USING FOR LOOP
num = int(input("Enter The Number:- "))
fac = 1
for i in range(1, num + 1):
    fac = fac * i
print(fac)

print()
## USING WHILE LOOP
n2 = int(input("Enter the number:- "))
fac2 = 1
i2 = 1
while i2 <= n2:
    fac2 = fac2 * i2
    i2 += 1
print(fac2)

