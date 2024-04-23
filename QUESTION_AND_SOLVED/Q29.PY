## WAP TO GENERATE EVEN NUMBERS IN GIVEN RANGE USING FOR LOOP AND WHILE LOOP?

## for loop
print("Code has Started")
print("This code is use to print all the even number in a given range:- ")
lower_limit = int(input("Enter lower limit number:- "))
uper_limit = int(input("Enter uper limit number:- "))

for i in range(lower_limit, uper_limit + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nCode has Ended")


print()
## while loop
print("Code has Started")
print("This code is use to print all the even number in a given range:- ")
lower_limit = int(input("Enter lower limit number:- "))
uper_limit = int(input("Enter uper limit number:- "))

while lower_limit <= uper_limit:
    if lower_limit % 2 == 0:
        print(lower_limit, end=" ")
    lower_limit += 1

print("\nCode has Ended")




