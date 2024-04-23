## JUMP STATEMENT
## break statement
## continue statement
## pass


## break statement
## example :- 
print("Start Break Statement:- ")
num = int(input("Enter any Number:- "))
count = 0
for i in range(1, num):
    if i > 10:
        break
    print(i)
    count = count + 1
    print(count)
if count == 10:
    print(count)


print()
print()

## example:- 
cn = int(input("Enter No. of Candy:- "))
av = 10
for i in range(1, cn + 1):
    if i > av:
        print("Out of Stok")
        break
    print("Candy")

print("End Break Statement")


print()
print()
print("Start Continue Statement:- ")
## continue statement
## 1
nm = int(input("Enter the Number:- "))
for i in range(1, nm):
    if i % 3 == 0:
        continue
    print(i)

print("end Continue Statement")


print()
print()
print("Start Continue Statement:- ")
## continue statement
## 1
nm = int(input("Enter the Number:- "))
for i in range(1, nm):
    if i == 15:
        continue
    print(i)

print("end Continue Statement")


print()
print()
print("Start Continue Statement:- ")
## continue statement
## 1
nm = int(input("Enter the Number:- "))
for i in range(1, nm):
    if i % 3 == 0 or i % 4 == 0:
        continue
    print(i)

print("end Continue Statement")


