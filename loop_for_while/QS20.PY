## WAP TO ENTER THE NUMBER TILL THE USER WANTS AND AT THE END IT SHOULD DISPLAY THE SUM OF ALL NUMBERS ENTERED?
## 123456 = 1 + 2 + 3 + 4 + 5 + 6 = 21

ch = "Y"
sum = 0
while ch.upper() == "Y":
    n = int(input("Enter any number:- "))
    sum += n
    ch = input("Do you wish to continue(Y,N)? :- ")
print("Sum of all the number is:- ", sum)