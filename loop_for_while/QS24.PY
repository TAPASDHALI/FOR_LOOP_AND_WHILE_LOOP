### WAP TO CONVERT BINARY TO DECIMAL.
bin = int(input("Enter a Binary Number: "))
dec = 0
p = 0
for i in range(bin):
    dec = dec + int(i) * pow(2,p)
    p = p + 1
print("Decimal number of binary", bin, "Number is: ", dec)