## WAP TO PRINT FIRST 10 INTEGERS AND  THEIR SQUARES USING WHILE LOOP?
# 1 == 1
# 2 == 4
# 3 == 9 AND SO ON

n = int(input("Enter any Number: "))
sq = 0
for i in range(1, n + 1):
    sq = i * i
    print(i, "*", i, "=", sq )

print()
#while loop
n1 = int(input("Enter any Number: "))
sq = 0
i = 1
while i <= n1:
    sq = i * i
    print(i, "*", i, "=", sq)
    i += 1