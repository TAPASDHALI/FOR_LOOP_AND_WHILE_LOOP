## WAP TO PRINT THE FACTORIAL OF A NUMBER ACCEPTED FROM USER?

## EXAMPLE:- 5 = 5*4*3*2*1 = 120
## EXAMPLE:-  6 = 6*5*4*3*2*1 = 720

## WHILE LOOP
num = int(input("Enter any Number:- "))
fac = 1
while num > 0:
    fac = fac * num
    num = num - 1
print("The Facturial Number is:- ", fac)

print()
## FOR LOOP
num = int(input("Enter Any Number:- "))
fac = 1
for i in range(1, num+1):
    fac = fac * i
print("Tne Factorial Number:- ", fac) 
