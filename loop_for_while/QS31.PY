## WAP TO DISPLAY SUM OF ODD NUMBERS AND EVEN NUMBERS SEPARATELY 
# THAT FALL BETWEEN TWO NUMBERS ACCEPTED THE USER(INCLUDING BOTH NUMBERS) USING WHILE LOOP?

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

se = 0
so = 0
if n1 > n2:
    while (n2 <= n1):
        if n2 % 2 == 0:
            se = se + n2
            n2 += 1
        else:
            so = so + n2
            n2  += 1 
else:
    while (n1 <= n2):
        if n1 % 2 == 0:
            se = se + n1
            n1 += 1
        else:
            so += n1
            n1 += 1
print("Sum of even number is:=> ", se)
print("Sum of odd number is:=> ", so)


print()
n3 = int(input("Enter first number: "))
n4 = int(input("Enter second number: "))

se1 = 0
so1 = 0
if n3 > n4:
    for i in range(n4, n3 + 1):
        if i % 2 == 0:
            se1 += i
        else:
            so1 += i

else:
    for j in range(n3, n4 + 1):
        if j % 2 == 0:
            se1 += j
        else:
            so1 += j

print("Sum of even number is:=> ", se1)
print("Sum of odd number is:=> ", so1)
