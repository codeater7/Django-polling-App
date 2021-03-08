class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'    # aafu lee ni add garna milxa; sap arguments ma matra aako pardainaa
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def fuckingRaiseAmount(cls, amount):            # automatically takes the (cls as the first amount) 
        cls.raise_amt = amount

    @classmethod
    def changeString(cls, emp_str):
        first1, last1, pay1 = emp_str.split('-')
        return (first1, last1, pay1)                          # return garnxaparxa, as it needs to be passed to constructor

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)      # no need for new
emp_2 = Employee('Test', 'Employee', 60000)

Employee.fuckingRaiseAmount(1.05)

Employee.fuckingRaiseAmount(1.06)       # class method call from the class

print("emp_1=> ",emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.changeString(emp_str_1)

print("access garna milyo constructor ko pani=>", new_emp_1.email)
print("access garxa, so like second constructor=>",new_emp_1.pay)



import datetime
my_date = datetime.date(2016, 7, 11)  # 2016-07-11


print(Employee.is_workday(my_date))