## WAP TO FIND THE SUM OF FOLLOWING SERIES 
## S = 1 + 4 - 9 + 16 - 25 + 36 - ..... N TERMS

n = int(input("Enter the term of the series: "))

s = 0
od = 0
ev = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        ev += (i**2)
    else:
        od += (i**2)
    s = ev - od
    
print(f'Sum of the series: {s}')

print()
## while loop
n2 = int(input("Enter the term of the series: "))

s2 = 0
od2 = 0
ev2 = 0
i1 = 2
while i1 <= n2:
    if i1 % 2 == 0:
        ev2 += (i1**2)
    else:
        od2 += (i1**2)
    i1 += 1
    s2 = ev2 - od2

print(f'Sum of the series: {s2}')