import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123password'



)

mycursor = mydb.cursor()
mycursor.exexcute('CREATE DATABASE testdb')


for db in mycursor:
    print(db)
