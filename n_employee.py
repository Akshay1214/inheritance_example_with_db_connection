# Creates class employee
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name        
        self.salary = salary

    def email_address(self):
        company = 'eclerx'
        email_address = self.first_name + '.' + self.last_name + '@' + company + '.com'
        return email_address

    def full_name(self):
        full_name = self.first_name + (" ") + self.last_name
        return full_name

    def apply_raise(self):
        apply_raise = self.salary * 0.15
        return apply_raise

# Creates class Developer 
class Developer(Employee):

    def __init__(self, first_name, last_name, salary, technologies):
        super().__init__(first_name, last_name, salary)
        self.technologies = [technologies]
                    
    def add_tech(self, tech):
        if (tech in self.technologies):
            print("Technology already present")
        else:
            self.technologies.append(tech)
    
    def display_technologies(self):
        return self.technologies

# Creates class Manager 
class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_reportee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_reportee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)            

    def display_reportee(self):
        return self.employees[0]    



# emp_1 = Employee('Akshay', 'Deokar', 1111111)
# print(emp_1.email_address())
# dev_1 = Developer("Rahul", "Shinde", 20000, "Java" )

# print(dev_1.display_technologies())
# dev_1.add_tech("Dot.Net")
# print(dev_1.display_technologies())
# dev_1.add_tech("Python")
# print(dev_1.display_technologies())
# dev_1.add_tech("C")
# print(dev_1.display_technologies())