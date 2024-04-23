## WAP TO FIND OUT GIVEN YEAR IS LEAP YEAR OR NOT?
year = int(input("Enter the Year:- "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

print()
print()
## short form
year = int(input("Enter the Year:- "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
