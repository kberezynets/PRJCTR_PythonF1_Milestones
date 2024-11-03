# python fetch_report.py april Engineering
# Report for Engineering department for April fetched.
# Total: 4
# Employees:
# - Apr 1, John Doe
# - Apr 10, Patrick Brown
# - Apr 11, John Wood
# - Apr 30, Helen King

import requests
import calendar

resp = requests.get('http://127.0.0.1:5000/DB')

monthDict = {month: index for index, month in enumerate(calendar.month_name) if month}

dept = input('Enter departnment: ')  # 'Engineering'
month = input('Enter month: ').capitalize()  #'april'

monthIndex = monthDict[month]

filtered_bdays = [
        employee for employee in resp.json()
        if (int(employee['birthday'].split('-')[1]) == monthIndex) and
           (employee.get('department') == dept)
    ]

sorted_bdays = sorted(filtered_bdays, key=lambda d: d['birthday'].split('-')[2])

print(f'Report for {dept} department for {month} fetched.')
print(f'Total: {len(filtered_bdays)}')

for e in sorted_bdays:
    print(f' - {month[0:3]} {e['birthday'].split('-')[2]}, {e['name']}')
