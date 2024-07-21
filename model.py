from wtforms import Form, BooleanField, StringField, PasswordField, validators,EmailField,SubmitField

import sqlite3

class RegistrationForm(Form):
    username = StringField('Username', [
        validators.Length(min=6, max=25, message='Username must be between 6 and 25 characters')])
    email = EmailField('Email', [
        validators.Email(message='Invalid email address')])
    password = PasswordField('Password', [
        validators.DataRequired(message='Password is required'),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit=SubmitField('Register')







def email_exists(email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    exists = cursor.fetchone()
    conn.close()
    return exists is not None
