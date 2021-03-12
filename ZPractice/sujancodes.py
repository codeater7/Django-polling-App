class Employee:

    noofEmployee = 0 
    payrise = 1.04


    def __init__(self, firstname, lastname, salary ):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = f'{firstname}_{lastname}@gmail.com'
        

        Employee.noofEmployee +=  1
        
        
    def summary_Employee(self):
        return f'{self.firstname} {self.lastname} with salary of {self.salary} '


    @classmethod                      # yo mathi ko variable chaange garna lai use garieeako
    def payrise(cls, amount):
        cls.payrise = amount
    
    def salary_with_increase(self):
         self.salary = self.salary * Employee.payrise
       
    

Emp1 = Employee("sujan", "pokharel", 2300)
Emp2 = Employee("Samikshya", "Aryal", 2400)

print(Emp1.summary_Employee())


print(Employee.payrise)
print(Emp1.__dict__)

print(Emp2.summary_Employee())
Emp2.payrise(1.5)
Emp2.salary_with_increase()

print( Emp2.summary_Employee())








      
    

    


    