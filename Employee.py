class Employee:
   def __init__(self, first_name, last_name, salary):
      company = 'eclerx'
      self.first_name = first_name
      self.last_name = last_name
      self.email_address = first_name + "." + last_name + '@' + company + '.com'
      self.salary = salary
   def full_name(self):
      full_name = self.first_name + (" ") + self.last_name
      return full_name
   def apply_raise(self):
      apply_raise = self.salary * 0.15
      return apply_raise  

class Developer(Employee):
   def __init__(self, first_name, last_name, salary, technologies):
      super().__init__(first_name, last_name, salary)
      self.technologies = technologies

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
      for emp in self.employees:
         print("Reportees are:- ", emp.full_name())

# dev_1 = Developer("Rahul", "Chavan", 10000, "ML")
# dev_2 = Developer("Mahesh", "Pawar", 15000, "AI")

# mng_1 = Manager("Prakash", "Shinde", 30000, [dev_1])
# print(mng_1.email_address)
# mng_1.display_reportee()