from flask import Flask, render_template, request, redirect, flash
# the "re" module will let us perform some regular expression operations
import re
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('flask.emailvalidation')
# now, we may invoke the query_db method

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def next():
    emails = mysql.query_db("SELECT * FROM emails")
    print("Fetched all friends", emails)
    if len(request.form['emails']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['emails']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        flash("Success!")
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES ( %(emails)s, NOW(), NOW());"
    data = {
             'emails': request.form['emails']
           }
    mysql.query_db(query, data)
    return render_template('success.html', emails=emails)


if __name__ == "__main__":
    app.run(debug=True)