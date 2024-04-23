## WAP TO FIND OUT THE MULTIPLICATION OF FIRST TO END NUMBERS?
## using for loop
print("Code has Started:- ")
num1 = int(input("Enter the first Number:- "))
num2 = int(input("Enter the End Number:- "))
res = 0
for i in range(num1, num2+1):
    res = num1 * i
print(f'Multiple of all the number in {num1} to {num2} are:-  {res}')
print("Code has Ended")