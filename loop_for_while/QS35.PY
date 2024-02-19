## WAP TO PRINT THE FOLOWING SERIES TILL N TERMS
## 1, 4, 9, 16, 25..... N TERMS?

n = int(input("Enter the series N terms from user: "))

for i in range(1, n + 1):
    print((i*i), end=" ")


print()
## while loop
n2 = int(input("Enter the series N terms from user: "))
i = 1
while i <= n2:
    print((i*i), end=" ")
    i += 1
    
    
