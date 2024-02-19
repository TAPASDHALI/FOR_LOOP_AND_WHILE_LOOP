## NESTED WHILE LOOP
i = 1
while i <= 3:
    print("Outer while loop:- ", i)
    i += 1
    j = 1
    while j <= 4:
        print("Inner while loop:- ", j)
        j += 1
print("Rest Of The Code")