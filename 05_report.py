# Write a program report.py that will take as arguments
# the database file name and month and will print the search result.

# python report.py database.csv april
# Report for April generated
# --- Birthdays ---
# Total: 45
# By department:
# - HR: 10
# - Finance: 15
# - Engineering: 20
# --- Anniversaries ---
# Total: 31
# By department:
# - Finance: 5
# - R&D: 10
# - Engineering: 16

# Optionally, implement -v (verbose) flag, which will also add employee names to the report.

import csv
import calendar

monthDict = {month: index for index, month in enumerate(calendar.month_name) if month}


def selebrations(filename, month):
    with open(filename, newline='') as file:

        reader = csv.reader(file)
        next(reader)

        employees = [line for line in reader]
        depts = set([e[2] for e in employees])

        monthIndex = monthDict[month.capitalize()]

        bdays = dict((d, 0) for d in depts)
        anniversaries = dict((d, 0) for d in depts)

        totalBdays = 0
        totalAnn = 0

        bdays_dept = '\nBy department:\n'
        ann_dept = '\nBy department:\n'

        for e in employees:
            if int(e[3].split('-')[1]) == monthIndex:
                bdays[e[2]] += 1
            if int(e[1].split('-')[1]) == monthIndex:
                anniversaries[e[2]] += 1

        for x in bdays:
            totalBdays += bdays[x]
            if bdays[x] > 0:
                bdays_dept += ' - ' + x + ':' + str(bdays[x])+'\n'

        for x in anniversaries:
            totalAnn += anniversaries[x]
            if anniversaries[x] > 0:
                ann_dept += ' - ' + x + ':' + str(anniversaries[x])+'\n'

        print(f'''Report for {month.capitalize()} generated
--- Birthdays ---
Total: {totalBdays}{bdays_dept}--- Anniversaries ---
Total: {totalAnn}{ann_dept}''')


selebrations('database.csv', 'april')
