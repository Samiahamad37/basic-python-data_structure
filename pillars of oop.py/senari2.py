

class Manager:
    def __init__(self, name, position, salary):
        self.name=name
        self.position=position
        self.salary=salary
    
    def update_salary(self,new_salary):
        self.salary=new_salary
        print(f"{self.name} new salary is {new_salary}")
        
        
    def display(self):
        print(f"{self.position} {self.name} your salary is {self.salary}")
    
obj1=Manager('samia','coder',300000)
obj1.update_salary(4000000)
obj1.display()
    