## WAP TO CREATE PERCENTAGE OF A STUDENT AND DISPLAY GREADE?
per = float(input("Enter Percentage:- "))

if per >= 85:
    print("Gread A+")
elif per >= 60 and per <= 84:
    print("Gread A")
elif per >= 45 and per <= 59:
    print("Gread B")
elif per >= 35 and per <= 44:
    print("Gread C")
else:
    print("Gread F")