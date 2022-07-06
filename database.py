# Importing Libraries
import sqlite3 
from employee import Employee, Developer, Manager

# Connecting to database
conn = sqlite3.connect('Mydatabase.db')
c = conn.cursor()

# Creating table in database
c.execute("""
    CREATE TABLE employees
    (first_name TEXT,
    last_name TEXT,
    salary INTEGER,
    email_address VARCHAR,
    technologies TEXT,
    reportee TEXT
    )""")
conn.commit()

first_name = input("Enter first name:-")
last_name = input("Enter last name:- ")
salary = int(input("Enter the employees salary:- "))
email = input("Enter the email id:- ")
technologies = input("Enter the technologies:- ")
reportees = input("Enter the reportee:- ")


emp_data = Employee(first_name, last_name, salary)
print(type(emp_data))
print(emp_data.first_name)
print(emp_data.last_name)
print(emp_data.salary)
print('='*80)

dev_data = Developer(first_name, last_name, salary, technologies)
print(dev_data.technologies)
print('='*80)

emp_data2=[reportees]
reportee = Manager(first_name, last_name, salary, emp_data2)
print(reportee.display_reportee())
print('='*80)
ab=[reportee]


c.execute("INSERT INTO employees VALUES (?,?,?,?,?,?)",(first_name, last_name, salary, email, technologies, reportees))

for item in c.execute("select * FROM employees"):
    print(item)

conn.commit()
conn.close()




























































































# # Inserting data in database table
# def insert_emp(emp):
#     with conn:
#         c.execute("INSERT INTO employees VALUES (:first_name, :last_name, :salary)", 
#                   {'first_name':emp.first_name, 'last_name':emp.last_name, 'salary':emp.salary})

# # Input which will be stored in database
# f_name = input("Enter first name:- ")
# l_name = input("Enter last name:- ")
# s_salary = input("Enter the salary: - ")

# emp_1 = Employee(f_name, l_name, int(s_salary))
# print("I am emp",(emp_1))
# insert_emp(emp_1)


# print(c.fetchall() )

# email = input("Enter the email :- ")
# technologies = input("Enter the technologies:- ")
# reportee = input("Enter the reportee:- ")
# emp_1 = Employee(f_name, l_name, s_salary, email)
# emp_1 = Developer(f_name, l_name, s_salary, technologies)
# emp_1 = Manager(f_name, l_name, s_salary, reportee)
# insert_emp(emp_1)
