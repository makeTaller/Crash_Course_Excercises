
class Employee():
    def __init__(self,f_name,l_name,salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self):
        e_raise = 5000
        new_salary = self.salary + e_raise
        print(new_salary)

jake = Employee('Jake','Fake',45000)

jake.give_raise()


