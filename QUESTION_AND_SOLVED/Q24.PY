## WAP TO FIND FIRST 15 FIBONACCI SERIES UP TO CREATION LIMIT IN VERTICAL?
n = int(input("Ente any Limits:- "))
a = 0
b = 1
c = 1
i = 1
print("Fibonnacci Series List:- ")
print(a, b, end=" ")
while i <= n:
    print(c, end=" ")
    a = b
    b = c
    c = a + b
    i += 1


print()
print()
## WAP TO FIND FIRST 15 FIBONACCI SERIES UP TO CREATION LIMIT IN VERTICAL?
n = int(input("Ente any Limits:- "))
a = 0
b = 1
c = 1
i = 1
print("Fibonnacci Series List:- ")
print(a, b, end=" ")
while i <= n:
    print(c, end=" ")
    a = b
    b = c
    c = a + b
    i += 1
    if i == 16:
        break