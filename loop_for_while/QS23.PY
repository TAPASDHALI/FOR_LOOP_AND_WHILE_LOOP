### WAP TO CONVERT DECIMAL TO BINARY.

num = int(input("Enter the positive Number: "))
bin = 0
p = 1
n = num

while n > 0:
    rem = int(n % 2)
    bin = bin + rem * p
    p = p * 10
    n = n/2
print("Binary Number of", num, "is", bin)