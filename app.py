from flask import Flask,render_template,request
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',
                               message="Registration Successful ✅",
                               message_type="success")
    else:
        return render_template('register.html',message="Email already exists 😵")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    verify = dbo.search(email,password)

    if verify:
        return render_template('loggedin.html')
    else:
        return render_template('login.html',
                               message="Invalid email or password",
                               message_type="error")
    

app.run(debug=True) # debug=True prevents from running again and again 