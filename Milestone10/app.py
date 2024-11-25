from flask import Flask, request, jsonify
import csv
import calendar


monthDict = {month: index for index, month in enumerate(calendar.month_name) if month}

# getting  data from .csv file and transfer to dictionary
with open('database.csv', newline='') as file:

    reader = csv.reader(file)
    keys = next(reader)
    DB = [line for line in reader]

    DB_dict = []
    id = 0

    for e in DB:
        employee = {'id': id}
        for i in range(len(keys)):
            employee[keys[i]] = e[i]
        DB_dict.append(employee)
        id += 1

app = Flask(__name__)


@app.get("/DB")
def get_DB():
    return jsonify(DB_dict)


@app.get("/birthdays")
def get_total_birthdays():
    department = request.args.get('department')
    month = request.args.get('month')
    monthIndex = monthDict[month.capitalize()]

    filtered_bdays = [
        employee for employee in DB_dict
        if (int(employee['birthday'].split('-')[1]) == monthIndex) and
           (employee.get('department') == department)
    ]

    return jsonify({
        "total": len(filtered_bdays),
        "employees": filtered_bdays
    })


@app.get("/anniversaries")
def get_total_anniversaries():
    department = request.args.get('department')
    month = request.args.get('month')
    monthIndex = monthDict[month.capitalize()]

    filtered_anns = [
        employee for employee in DB_dict
        if (int(employee['hiring date'].split('-')[1]) == monthIndex) and
           (employee.get('department') == department)
    ]

    return jsonify({
        "total": len(filtered_anns),
        "employees": filtered_anns
    })


if __name__ == '__main__':
    app.run(debug=True)
