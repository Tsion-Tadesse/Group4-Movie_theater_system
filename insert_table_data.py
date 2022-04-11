import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="MOVIE_THEATER_DB")


mycursor = mydb.cursor()

sqlform = "Insert into account(fname, lname, user_id, password ) values (%s, %s, %s, %s)"

Account = [("john", "smith", "jsmith", "jsmith1")]

mycursor.execute(sqlform, Account)

mydb.commit()