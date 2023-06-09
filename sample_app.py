import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE')
)
mycursor = mydb.cursor()
mycursor.execute("SELECT id,status FROM leave_table")
myresult = mycursor.fetchall()
print(myresult)