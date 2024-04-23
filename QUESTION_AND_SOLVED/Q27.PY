## WAP TO FIND OF THE NUMBER IS A AUTOMORPHIC NUMBER OR NOT?
## 5 = 5 * 5 = 25 = LAST DIGITS ARE SAME OF A 5
## 6 = 6 * 6 = 36 = LAST DIGITS ARE SAME OF A 6
## 76 = 76 * 76 = 5776 = LAST DIGITS ARE SAME OF A 76
## SO THOSE NUMBER ARE CALLED AUTOMORPHIC NUMBER
num = int(input("Enter any Number:- "))
sqr = num * num
f = 0
temp = sqr
n = 10
while temp > 0:
    rem = sqr % n
    if num == rem:
        f = 1
        break
    temp //= 10
    n = n * 10

if f == 1:
    print("Number is a Automorphic Number")
else:
    print("Number is Not a Automorphic Number")


## WAP TO PRINT FIRST 5 AUTOMORPHIC NUMBER?
num2 = int(input("Enter the start number:- "))
num3 = int(input("Enter the last number:- "))
count = 0
while num2 != num3:    
    sqr2 = num2 * num2
    temp2 = sqr2
    f2 = 0
    n2 = 10
    while temp2 > 0:
        rem2 = sqr2 % n2
        if rem2 == num2:
            f2 = 1
            break
        temp2 //= 10
        n2 = n2 * 10
    if f2 == 1:
        # print(f'{num2} is a Automorphic Number')    
        count = count + 1
        if count == 5:
            break
        num2 += 1
    

