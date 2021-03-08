class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):   # programming language naya add vayo; paila ko ni sap rakhna paryo
        super().__init__(first, last, pay) 
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):     # default rakhyo employees= none
        super().__init__(first, last, pay)                    #  parent class ko constructor lerauna paryo vani,  # but self chaidaina
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:          # not in 
            self.employees.append(emp)         # append()

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):                        # print ta garna paryo, instance ko ho so self
        for emp in self.employees:
            print('-->', emp.fullname())         # how fullname ? 


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.fullname())
print(dev_1.apply_raise())                                                     # Why None   ????????


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)

print(mgr_1.print_emps())

mgr_1.remove_emp(dev_2)

mgr_1.print_emps()