# palindrome words
a=input("Enter a string: ")
if a==a[::-1]:
 print(a,"is a palindrome")
else:
  print(a ,"is not a palindrome") 
  
  
  
  # to determine the greater value
  x=float(input("enter 1st no: "))
y=float(input("enter 2nd no: "))
if x>y:
    print("x is a graeter no")
else :
    print("y is a greater no")  
    
    
    
    # prime no determination
    x=int(input("Enter a number: ")) 
if x==2 or x==3 or x==5 or x==7 :
    print( x, "is a prime number")
elif x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
    print(x,"is a prime number")
else:
    print(x ,"is not a prime number")      