## WAP TO FIND THE SUM OF THE FOLLOWING SERIES(ACCEPT VALUE OF X AND N FROM USER)

## EXAMPLE:- 1 + X/1! + X^2/2! +.....+ X^N/ N! TERMS?

n = int(input("Enter the term of the series number from user: "))

x = 1
ssum = 0
for i in range(1, n + 1):
    ssum += 1 + (x*i)/(i*i)
print(f'Sum of the series from user dependend: {ssum}')

print()
## while loop?

n2 = int(input("Enter the term of the series number from user: "))

x1 = 1
ssum1 =  0
i = 1
while i <= n2:
    ssum1 += 1 + (x*i)/(i*i)
    i += 1
print(f'Sum of the series from the user dependend: {ssum1}') 