x=int(input("enter the 1st number: "))
y=int(input("enter the 2nd number: "))
z=input("enter the operation: ")
match z :
    case"+":
        print(x+y)

    case"-":
        print(x-y)

    case"*":
        print(x*y)

    case"/":
        if y==0:
            print("enter 2nd number")
        else:    
           print(x/y)
    case _:
        print("invalid operator")        
             