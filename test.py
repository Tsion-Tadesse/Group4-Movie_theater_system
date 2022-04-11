from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="MOVIE_THEATER_DB")


mycursor = mydb.cursor()

app = Flask(__name__)
@app.route("/")
def movie_result():

    movie_name = input("Enter the movie name:" )
    print(movie_name)
    return movie_name.upper()
f = open ('homepage.html', 'r')

f.read()
f.close()