## WAP TO PRINT FIBONACCI SERIES UP TO CERTIAIN LIMIT?
## EXAMPLE:- 0 1 1 2 3 5 8 13 21 34 55 89 .........
limit = int(input("Enter the number:- "))
a = 0
b = 1
c = 1
print('Fibonacci Series')
# print(a)
# print(b)
# for c in range(1, limit + 1):
while c <= limit:
    print(c, end=" ")
    a = b
    b = c
    c = a + b
