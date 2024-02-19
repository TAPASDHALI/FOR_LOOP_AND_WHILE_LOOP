## WAP TO ENTER THE NUMBERS TILL THE USER ENTER ZERO AND ---
## AT THE END IT SHOULD DISPLAY THE COUNT OF POSITIVE OR NEGATIVE NUMBERS ENTERED?

ch = "Y"
sump = 0
sumn = 0
num = 1
while (num!=0) and ch.upper() == "Y":
    num = int(input("Enter any number:- "))
    if num > 0:
        sump += num
    else:
        sumn += num
print(f'Sum of all the positive numbers is :=> {sump}')
print(f'Sum of all the negative numbers is :=> {sumn}')
