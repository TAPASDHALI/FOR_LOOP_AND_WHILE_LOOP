## WAP TO ACCEPT 10 NUMBERS FROM THE USER AND DISPLAY THE LARGEST AND SMALLEST NUMBER?
## for loop
l = []
for i in range(10):
    num = int(input("Enter the ten digits numbers: "))
    l.append(num)
l.sort()
print(l)
print("Largest number is: ", l[-1])
print("Smallest number is: ", l[0])

print()
## while loop
l1 = []
i = 0
while i < 10:
    num1 = int(input("Enter the ten digits numbers: "))
    l1.append(num1)
    i += 1
l1.sort()
print("Largest number is: ", l1[-1])
print("Smallest number is: ", l1[0])