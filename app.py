from sample_app import mycursor, mydb


def my_new_table():
    stm=mycursor.execute("CREATE TABLE IF NOT EXISTS my_new_table (id INT PRIMARY KEY, description VARCHAR(255), start_date DATE, end_date DATE, status VARCHAR(30))")
    mycursor.execute("SELECT * FROM my_new_table")
    print(stm)

def approve_leave(id):
    mycursor.execute("UPDATE my_new_table SET status = 'Approved' WHERE id = %s;", (id,))
    mydb.commit()
    return ({"Status": "Leave approved successfully"})


def reject_leave(id):
    mycursor.execute("UPDATE my_new_table SET status = 'rejected' WHERE id = %s;", (id,))
    mydb.commit()
    return ({"Status": "Leave Rejected"})


def delete_record(id):
    delete_query = f'''Delete  from my_new_table where id = {id}'''
    mycursor.execute(delete_query)
    mydb.commit()
    return "User has been deleted sucessfully"

def insert_record():
    sql = "INSERT INTO my_new_table (id, description, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s)"
    val = (6, "cold", "2022-10-12", "2022-10-15", "pending")
    mycursor.execute(sql, val)
    mydb.commit()
    return "record has been inserted sucessfully"


def print_table():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM my_new_table")
    myresult = mycursor.fetchall()
    output = ''
    for x in myresult:
        output += str(x)
    return output

def status():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id, description,status FROM my_new_table")
    myresult = mycursor.fetchall()
    output = ''
    for x in myresult:
        output += str(x)
    return output


def status_type(id):
    mycursor.execute("SELECT status FROM my_new_table WHERE id = %s;", (id,))
    myresult = mycursor.fetchone()
    return myresult

