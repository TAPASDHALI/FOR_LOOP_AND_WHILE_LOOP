## WAP TO FIND THE HFC OF TWO NUMBERS ENTERED FROM THE USER
n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

if n1 > n2:
    mn = n2
else:
    mn = n1

for i in range(1, mn+1):
    if n1 % i == 0 and n2 % i == 0:
        hcf  = i
print(f'The HCF/GCD of these two numbers is : {hcf}')

print()
##while loop
n3 = int(input("Enter 1st Number: "))
n4 = int(input("Enter 2nd Number: "))

if n3 > n4:
    mn = n4
else:
    mn = n3
i = 1
while i < mn:
    if n3 % i == 0 and n4 % i == 0:
        hcf1  = i
    i += 1
print(f'The HCF/GCD of these two numbers is : {hcf1}')