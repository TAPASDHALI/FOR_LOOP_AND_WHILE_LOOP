## WAP TO FIND THE MULTIPLY(PRODUCT) OF THE DIGITS OF A NUMBER ACCEPTED FROM THE USER:- 
## example:-  2345
## 2 * 3 * 4 * 5 = 120

n = int(input("Enter any number: "))
res = 0
mul = 1
while n > 0:
    res = n % 10
    mul = mul * res
    n = n // 10
print(f'Product of the digit are:- {mul}')

print()
## USE FOR LOOP
n1 = input("Enter any digits Number: ")
mul1 = 1
for i in range(0, len(n1)):
    mul1 = mul1 * int(n1[i])
print(f'Multiply of the digits are: {mul1}')