import mysql.connector

mydb = mysql.connector.Connect(host="localhost", user="root", password="bala84126@")
print(mydb)

if(mydb):
    print("connected")
else:
    print("failed")
