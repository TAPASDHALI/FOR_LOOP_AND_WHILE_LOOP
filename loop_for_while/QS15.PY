## WAP TO DISPLAY THE NUMBER NAMES OF THE DIGITS OF A NUMBER ENTERED BY USER,
## FOR EXAMPLE IF THE NUMBER IS 231 THEN OUTPUT SHOULD BE TWO THREE ONE

num = input("Enter any Number:- ")
l1 = list(num)
print(l1)
l = len(l1)
print(l)
i = 0
n = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
while (i<l):
    print(n[int(l1[i])], end=" ")
    i = i + 1