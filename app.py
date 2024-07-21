from flask import Flask,render_template,redirect,request,url_for
import bcrypt
from model import RegistrationForm,email_exists
from wtforms import validators
import sqlite3

app= Flask(__name__,template_folder="templates")


@app.route('/')
def home():
    return render_template('home.html')




















@app.route('/login',methods=["POST","GET"])
def loginpage():
    if request.method=="POST":
        email=request.form.get('email')
        if email_exists(email):
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            conn.close()
            if user:
                stored_hashed_password = user[0]
                password=request.form.get('password')
                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                    return redirect('/')
                else:
                     return render_template('login.html',error=True)
        else:
            return render_template('login.html')
    return render_template('login.html')






















@app.route('/signup',methods=["GET","POST"])
def signupage():
    if request.method=="POST":
        email=request.form.get('email')
        if email_exists(email):
            return render_template('signup.html',error=True)
        else:
            username = request.form['username']
            password = request.form['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", 
                           (username, email, hashed_password))
            cursor.execute(f"create table {username} (name text not null, date_cre date not null,descrption text not null);")
            conn.commit()
            conn.close()
            return redirect(url_for('loginpage'))
    else:
         return render_template('signup.html')

        


if __name__=="__main__":
    app.run(debug=True)