## WAP TO DISPLAY ALL THE NUMBERS WHICH ARE DIVISIBLE 
# BY 13 BUT NOT 3 BETWEEN 100 AND 500.(EXCHUSIVE)

n1 = 101

while (n1 <= 500):
    if n1 % 13 == 0 and n1 % 3 != 0:
        print(n1, end=" ")
    n1 + 1