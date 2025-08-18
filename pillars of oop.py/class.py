# class Addition:
#     def __init__(self, firstno,secno,thirdno):
#        self.firstno=firstno
#        self.secno= secno
#        self.thirdno=thirdno
#     def sum(self):
#         print (self.firstno + self.secno + self.thirdno)
#     def sub(self):
#         print (self.firstno - self.secno -self.thirdno)
       
        
# object = Addition ( 4,5,6)
# object.sum()
# object.sub()
            
            
# class Charmy:
#     total=0
    
#     def __init__ (self, name, age):
#         self.name=name
#         self.age=age
#         Charmy.total +=1
        
#     def intro(self):
#         print(f"my name is {self.name} am {self.age}yrs old ,we'r {Charmy.total} in the class")
        
# obj=Charmy("SAMIA",20)
# obj.intro()

        
# class You:
#     jina="Irfan"
    
    
#     def __init__(self, name):
#         self.name=name
        
        
#     def intro(self):
#         print(f"my name is {self.name}")
     
#     @classmethod   
#     def introduction(cls):
#          print(f"my name is {You.jina}")
        
# obj=You("samia")
# obj.intro()
# obj.introduction()      
        
    
        
        
# class A:
#     def __init__(self, name):
#         self.name=name
        
#     def intro(self):
#         print(f"am your parentes A {self.name}")

# class B(A):
#     def __init__(self,name):
#         self.name= name 
#     def yr(self):
#          print(f"am your child B {self.name}") 

# # obj=A("SAMIA")
# obj=B("mama")
# obj.intro()
# # obj.yr()

     
     
class A:
    def __inti__(self, name, age):
       self._name=name
       self.age=age
       
    # def get_name(self):
    #     get._name=name
        
          
          
class B(A):
    def into(self):
           print(f"am  {self._name} is {self.age}") 
            
obj=A("samia", 20)
obj.into()
        
        
        