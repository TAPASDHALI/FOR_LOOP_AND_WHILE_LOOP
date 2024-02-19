## WAP TO ACCEPT 10 NUMBERS FROM USER AND DISPLAY IT'S AVERAGE?

sum = 0
i = 0
while i < 10:
    num = int(input("Enter any Number: "))
    sum = sum + num
    i += 1
print("Average is: ", sum/10)

print()
# for loop
sum = 0
for i in range(1, 10 +1):
    num = int(input("Enter any Number: "))
    sum += num
print("Average is: ", sum/10)

# print()
# # wap to print the foloowing series in for loop?
# ## 10 20 30... .... 300
# n = int(input("Enter any number:- "))
# i = 1
# while i <= n:
#     if i % 10 == 0:
#         print(i, end=" ")
#     i += 1
    
