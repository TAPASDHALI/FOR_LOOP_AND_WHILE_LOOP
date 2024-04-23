## WAP TO INPUT A NUMBER AND PRINT IT IS FIRST FIVE MULTIPLES?
num = int(input("Enter any number:- "))
print(num*1)
print(num*2)
print(num*3)
print(num*4)
print(num*5)
print(num*6)
print()

## USING FOR LOOP
print("Using For Loop")
num1 = int(input("Enter any number:- "))
t = int(input("Do you want how many Times:- "))
for i in range(1, t + 1):
    print(num1*i, end=" ")

print()
## WHILE LOOP
print("USED WHILE LOOP")
n = int(input("Enter any number:- "))
tm = int(input("Do you want how many Times:- "))
j = 0
while j > tm:
    print(n * j)
    j += 1