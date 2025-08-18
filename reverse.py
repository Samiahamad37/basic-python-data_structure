x=input("enter a string: ")
y=x[::-1]
print(y)


# determining the access of the licences
x=input("enter name: ")
y=int(input("enter age: "))
if y>18:
  print("eligible to apply for a driving licence")
else:
   print("not eligible to apply for a driving licence")




x=input("enter the word: ")
y="a",'e',"i","o","u"
b=len(y)
if (y) in (x):
  print(len(y))
else: 
  print("null")  


# determining a leap yr
x=int(input("enter a year: ")) 
if x%4==0 and x%100==0:
 print(x,"is a leap year")
else :
 print(x," is not a leap year ")