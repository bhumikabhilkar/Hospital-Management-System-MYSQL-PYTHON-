import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='Hospital')

#create cursor object
cur=mydb.cursor()


s="create table Patients (Patient_ID int, Medicine_ID int, Entry_Date date ,Exit_Date date)"
#YYYY-MM-DD
#call function to execute 
cur.execute(s)
m="create table Medicines ( Medicine_ID int, Medicine_Name varchar(50),Quantity int)"
#call function to execute 
cur.execute(m)  