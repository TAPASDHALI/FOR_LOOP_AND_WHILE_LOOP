## WAP TO PERFORM ALL MATHEMATICAL OPERATORS OF A SIMPLE CALCULATOR FROM USER?
n1 = int(input("Enter any Number:- "))
n2 = int(input("Enter any Number:- "))
op = input("Enter Mathematical operator:- ")
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '**':
    print(n1 ** n2)
elif op == '/':
    print(n1 / n2)
else:
    print('Rest Of the Code')