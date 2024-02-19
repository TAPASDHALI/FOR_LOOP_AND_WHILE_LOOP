## WAP TO FIND SUM OF EVEN DIGITS AND PRODUCT OF ODD DIGITS OF A GIVEN NUMBERS?

# EXAMPLE : GIVEN NUMBER : 123456789
## EVEN NUMBER : 2 + 4 + 6 + 8 = 20
## ODD NUMBER : 1 * 3 * 5 * 7 * 9 = 945

n = int(input("Enter any Number: "))
res = 0
sum = 0
product = 1
while n > 0:
    res = n % 10
    if res % 2 == 0:
        sum += res
    n = n // 10
print(sum)

print()
n1 = int(input("Enter any Number: "))
res = 0
product = 1
while n1 >0:
    res = n1 % 10
    if res % 2 != 0:
        product = product * res
    n1 = n1 // 10
print(product)
