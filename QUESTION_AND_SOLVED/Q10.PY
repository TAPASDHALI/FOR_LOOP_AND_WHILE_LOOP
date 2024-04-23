## WAP TO FIND LARGEST NUMBER AMONG THREE INPUTED NUMBERS FROM USER?
n = int(input("Enter the 1st number:- "))
n2 = int(input("Enter the 2nd number:- "))
n3 = int(input("Enter the 3rd number:- "))

if n > n2 and n > n3:
    print(f'{n} is the Largest Number and its position is N')
elif n2 > n and n2 > n3:
    print(f'{n2} is the Largest Number and its position is N2')
else:
    print(f'{n3} is the Largest Number and its position is N3')