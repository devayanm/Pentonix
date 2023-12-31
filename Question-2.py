from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
departments = {
    10: "Admin",
    20: "Accounts",
    30: "Sales",
    40: "Marketing",
    50: "Purchasing"
}

employees = {
    1: {"name": "Amal", "dno": 10, "salary": 30000},
    2: {"name": "Shyamal", "dno": 30, "salary": 50000},
    3: {"name": "Kamal", "dno": 40, "salary": 10000},
    4: {"name": "Nirmal", "dno": 50, "salary": 60000},
    5: {"name": "Bimal", "dno": 20, "salary": 40000},
    6: {"name": "Parimal", "dno": 10, "salary": 20000}
}

# API to get employee details by ENO
@app.route('/api', methods=['GET'])
def get_employee_by_eno():
    eno = int(request.args.get('ENO'))
    if eno in employees:
        return jsonify(employees[eno])
    else:
        return jsonify({"error": "Employee not found"}), 404

# API to get list of employees by DNAME
@app.route('/api/dname', methods=['GET'])
def get_employees_by_dname():
    dname = request.args.get('DNAME')
    dno_list = [dno for dno, name in departments.items() if name == dname]
    result = []
    for eno, emp_data in employees.items():
        if emp_data['dno'] in dno_list:
            result.append(emp_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=9000)
