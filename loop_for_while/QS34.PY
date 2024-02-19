## WAP TO PRINT THE FOLLOWING SERIES TILL N TERMS 
## 2, 22, 222, 2222----- N TERMS?
# for loop

n = int(input("Enter the series number: "))
s = "2"
for i in range(1, n + 1):
    print(s, end=" ")
    s = s + "2" 

print()
# while loop
n1 = int(input("Enter the series number: "))
s1 = "2"
i = 0
while i < n1:
    print(s1, end=" ")
    s1 = s1 + "2"
    i += 1


