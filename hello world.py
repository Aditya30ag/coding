a=int(input("THE FIRST NUMBER"))
b=int(input("THE SCOND NUMBER"))
operator=input("+,-,*,/")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("INVALID OPERATION")