## WAP TO PRINT CALCULATE THE NETSALARY?
## NET SALARY CALCULATE
## IF SALARY IS MORE 80,000 IF DEDUCT 10%
## IF SALARY IS MODE 50,000 IF DEDUCAT 7% OF SALARY
## IF SALARY IS MORE 20,000 IF DEDUCAT 5% OF SALARY
## IF SALARY IS LESS 20,000 IF NOT DEDUCAT 
sal = int(input("Enter Your Salary:- "))
if sal >= 80000:
    netsal = sal - (sal*0.1)
elif sal >= 50000:
    netsal = sal - (sal*0.07)
elif sal >= 20000:
    netsal = sal - (sal*0.05)
else:
    netsal = "Salary less then 20000"
print("Your Net Salary is:- ", netsal)