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

# Taking inputs
first_name = input("Enter first name:- ")
last_name = input("Enter last name:- ")
salary = int(input("Enter the employees salary:- "))
technologies = input("Enter the technology:- ")
reportees = input("Enter the reportee:- ")

emp_data = Employee(first_name, last_name, salary)
emp_email = emp_data.email_address()

dev_data = Developer(first_name, last_name, salary, technologies)
dev_data = Employee(first_name, last_name, salary)
dev_email = dev_data.email_address()

add_to_tech = input("Any more technologies to add:- ")
dev_data = [add_to_tech]
tech_to_add = Developer(first_name, last_name, salary, add_to_tech)
tech = technologies + "," + add_to_tech

emp_data2=[reportees]
reportee = Manager(first_name, last_name, salary, emp_data2)

# Inserting data to database
c.execute("INSERT INTO employees VALUES (?,?,?,?,?,?)",(first_name, last_name, salary, dev_email, tech, reportees))

for item in c.execute("select * FROM employees"):
    print(item)

# Closing connection
conn.commit()
conn.close()