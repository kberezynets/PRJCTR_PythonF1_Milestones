# Create a program generate_data.py, and write data to database.csv file.
# You can generate arbitrary information about employees, but be sure
# to include name, hiring date, department, and birthday

# To make data realistic you can either predefine the pool of names,
# and use random module, or use the Faker package
# (you need to install it with pip install Faker

import csv
from faker import Faker
import random

fake = Faker()

header = ['name', 'hiring date', 'department', 'birthday']
dept = ['HR', 'Finance', 'Engineering', 'R&D']
data_base = []

for _ in range(100):
    data_base.append(
        [fake.name(),
         fake.date_this_decade(),
         random.choice(dept),
         fake.date_of_birth(minimum_age=18, maximum_age=60)
         ])

with open('database.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data_base)

# with open('database.csv', 'r') as file:
#     t6 = file.read()

# print(t6)
