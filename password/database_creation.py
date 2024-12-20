import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='root')

#create cursor object
cur=mydb.cursor()
#call function to execute 
cur.execute("CREATE DATABASE HOSPITAL")