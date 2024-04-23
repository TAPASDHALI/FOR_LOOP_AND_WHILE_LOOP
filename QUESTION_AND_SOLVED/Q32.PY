## WAP TO MULTIPLICATION ALL THE NUMBER IN GIVEN RANGE USING FOR LOOP AND WHILE LOOP?

## for loop
print("Code has Started")
print("This code is use to print all the even number in a given range:- ")
lower_limit = int(input("Enter lower limit number:- "))
uper_limit = int(input("Enter uper limit number:- "))

sum = 1
for i in range(lower_limit, uper_limit + 1):
    sum = sum * i
print(f'Sum of all the number are:- {sum}')

print("\nCode has Ended")


print()
## while loop
print("Code has Started")
print("This code is use to print all the even number in a given range:- ")
lower_limit = int(input("Enter lower limit number:- "))
uper_limit = int(input("Enter uper limit number:- "))

sum = 1
while lower_limit <= uper_limit:
    sum = sum * lower_limit
    lower_limit += 1
print(f'Sum of all the number are:- {sum}')

print("\nCode has Ended")