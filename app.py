from flask import Flask, render_template, request,session
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<name>",methods=['GET','POST'])
def login(name):
    return render_template(f'{name}.html')


# google account show profileIdentifier


if __name__=="__main__":
    app.run()