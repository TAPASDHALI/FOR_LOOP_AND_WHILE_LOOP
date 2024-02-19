## WAP TO CHECK WHETHER A NUMBER IS PALINDROME OR NOT?
## EXAMPLE =  121, 11, 414, 313, 131, 74747, 12121, 
### STRING:-  MOM, DAD, MADAM, REFER,


n = int(input("Enter any number:=> "))
temp = n
r = 0
rn = 0
len = len(str(n))
i = 0
while (i<len):
    r = n % 10
    rn = rn * 10 + r
    n = n // 10
    i = i + 1
if temp == rn:
    print("Number is Palindrome")
else:
    print("Number is not a Palindrome")