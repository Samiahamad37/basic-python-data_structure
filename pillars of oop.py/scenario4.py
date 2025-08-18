class Car:
    def __init__(self,make ,model,year ,is_rented=False):
        self.make=make
        self.model=model
        self.year=year
        self.is_rented=is_rented
        
    def display(self):
        print(f"the car is {self.make} {self.model} of {self.year} ")
        if  self.is_rented:
                print(f'{self.make}, {self.model} is not available')
        else:
            print(f'{self.make} ,{self.model} is availabe')
       
        
    def rent_car(self):
        
        if self.is_rented:
             print(f"the {self.make} {self.model} is not available hence renting denied")
        else:
              print(f"you have successed to rent {self.make} {self.model} of {self.year}")
             
              
    def return_car(self):
        if  self.is_rented:
              print(f"{self.make} {self.model} of  {self.year} was not rented")
        else:
              print(f"{self.make}, {self.model} of {self.year} has successful returned")
          
        
    
        
obj=Car("toyota","corolla",2020 ,True)
obj.display()
obj.rent_car()
# obj.rent_car()ss
# obj.return_car()
           
        