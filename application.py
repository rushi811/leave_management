from flask import Flask, jsonify, request
from app import approve_leave, reject_leave,insert_record,delete_record,print_table,status_type,status

app = Flask(__name__)
   
@app.route('/')
def table_view():
    result = print_table()
    return jsonify(result)

@app.route('/approve_leave/<int:id>', methods=['POST'])
def approve_leave_route(id):
    result = approve_leave(id)
    return jsonify (result)

@app.route('/reject_leave/<int:id>', methods=['POST'])
def reject_leave_route(id):
    result = reject_leave(id)
    return jsonify (result)


@app.route('/add_records', methods=['POST'])
def view_records_route():
    result = insert_record()
    return jsonify(result)

@app.route('/delete_record/<int:id>', methods=['POST'])
def delete_my_record(id):
    result = delete_record(id)
    return jsonify(result)

@app.route('/status',methods=['POST'])
def status_view():
    result = status()
    return jsonify(result)


@app.route('/status/<int:id>',methods = ['POST'])
def get_status_type(id):
    result = status_type(id)
    return jsonify(result)
    


if __name__ == '__main__':
    app.run(debug=True)