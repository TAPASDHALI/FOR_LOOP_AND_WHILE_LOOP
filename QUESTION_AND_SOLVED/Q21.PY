## WAP TO CHECK IS EMAIL AND PASSWORD IN CURRECT OR NOT IN PYTHON USER DEFINE?
email1 = "gobaindo3341@gmail.com" 
password = "1234"
if email1 == "gobaindo3341@gmail.com":
    if password == "1234":
        print("Welcome Email:- ", email1)
    else:
        print("Wrong Password")
else:
    print("Wrong Email Id")

## check again
eml = input("Enter the Email ID:- ")
if eml== "global@gmail.com":
    pwd = input("Enter the password:- ")
    if pwd == "12345":
        print("Welcome To Email ID:- ", eml)
    else:
        print("Wrong Password")
else:
    print("Wrong Email Id")