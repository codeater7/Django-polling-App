class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'    # aafu lee ni add garna milxa; sap arguments ma matra aako pardainaa
        self.pay = pay

        Employee.num_of_emps += 1                 # Constructor ma class variable pani add garna milxa

    def fullname(self):                                 # full-name nikalyo
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):                                  # Apply raise garyo 
        self.pay = int(self.pay * self.raise_amt)          # Most important => self.... tara sabbai badauna ko lagi Employee.raise amount garako vayee huni

   

    @classmethod
    def increasPayPercent(cls, amount):            # class method => (cls as the first amount) 
        cls.raise_amt = amount

    @classmethod                                # Second/ Alternative  constructor pani vaninxa, 
    def changeString(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return  cls (first, last, pay )             # ALways needs to be returned ; Alternative constructor                      

    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# emp_1 = Employee('Corey', 'Schafer', 50000)      # no need for new

# emp_2 = Employee('Test', 'Employee', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

StrEmp1 = Employee.changeString(emp_str_1)
print(StrEmp1.email)

print(StrEmp1.__dict__)



# print(StrEmp1.fullname())




# Employee.increasPayPercent(1.05)

# Employee.increasPayPercent(1.06)       # class method call from the class

# print("emp_1=> ", emp_1.raise_amt)    
# print(emp_1.increasPayPercent(2))   # we increased it by 2 but for rest it is 1.06
# print( emp_1.__dict__)
# (emp_1.apply_raise())
# print( emp_1.__dict__)
# print( emp_2.__dict__)





#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.changeString(emp_str_1)

# print("access garna milyo constructor ko pani=>", new_emp_1.email)
# print("access garxa, so like second constructor=>",new_emp_1.pay)



# import datetime
# my_date = datetime.date(2016, 7, 11)  # 2016-07-11


# print(Employee.is_workday(my_date))

print(Employee.num_of_emps)