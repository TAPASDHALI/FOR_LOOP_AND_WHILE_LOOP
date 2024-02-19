## WAP TO REVERSE THE NUMBER ACCEPTED FROM USER USING WHILE LOOP:- 

## EXAMPLE:- 12345  = 54321
## 
n = int(input("Enter any Number: "))
i = 0
rev = 0
while n > 0:
    i = n % 10
    rev = (rev * 10) + i
    n = n // 10
print(f'The reverse Number are: {rev}')

print()
## for loop
n1 = input("Enter any Number: ")
rev1 = " "
for i in range(len(n1), 0, -1):
    rev1 += n1[i-1]
print(f'Reverse Number are: {rev1}')